from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Vendor(models.Model):  # class Vendor 繼承 django.db.models.Model
    vendor_name = models.CharField(max_length=20)  # 攤販的名稱
    store_name = models.CharField(max_length=10)  # 攤販店家的名稱
    phone_number = models.CharField(max_length=20)  # 攤販的電話號碼
    address = models.CharField(max_length=100)  # 攤販的地址
    # 覆寫 __str__

    def __str__(self):
        return self.vendor_name


class Food(models.Model):
    food_name = models.CharField(max_length=30)  # 食物名稱
    price_name = models.DecimalField(max_digits=3, decimal_places=0)  # 食物價錢
    # 儲存十進制的數字，後面參數分別代表 最大長度 及 小數點後方的位數
    food_vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE)  # 代表這食物是由哪一個攤販所做的
    # 在 Django中是 多對一(many-to-one)的關聯，而前方的參數代表的意思就是對應到哪一個類別，這裡對應到的是 Vendor，而後方的 on_delete 代表的是當對應的類別被刪除之後，這些對應到別人的資料要怎麼被處理，而 CASCADE 就是一倂刪除

    def __str__(self):
        return self.food_name


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Vendor._meta.fields]


'''
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Food._meta.fields]
    list_filter = ('price_name',)
# 自行宣告 類別
'''


class Morethanfifty(admin.SimpleListFilter):

    title = _('price')
    parameter_name = 'compareprice'  # url最先要接的參數

    def lookups(self, request, model_admin):
        return (
            ('>50', _('>50')),  # 前方對應下方'>50'(也就是url的request)，第二個對應到admin顯示的文字
            ('<=50', _('<=50')),
        )
    # 定義查詢時的過濾條件

    def queryset(self, request, queryset):
        if self.value() == '>50':
            return queryset.filter(price_name__gt=50)
        if self.value() == '<=50':
            return queryset.filter(price_name__lte=50)


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Food._meta.fields]
    # 將 Morethanfifty 填入
    list_filter = (Morethanfifty,)
