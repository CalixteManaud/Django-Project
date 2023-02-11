from django.contrib import admin
from World_Cup.models.Registration import Registration
from World_Cup.models.AllsProducts import Category, Product, Commande
from World_Cup.models.AllProductsFootball import CategoryFoot, ProductFoot, CommandeFoot
from World_Cup.models.AllProductsNFL import CategoryNFL, ProductNFL, CommandeNFL

admin.site.site_header = 'E-Commerce World Cup'
admin.site.site_title = 'Shop World Cup'
admin.site.index_title = 'Bienvenue dans le back office'


class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'date_added')


class AdminProduct(admin.ModelAdmin):
    list_display = ('titre', 'price', 'category', 'date_added')
    search_fields = ('titre',)
    list_editable = ('price',)


class AdminCommande(admin.ModelAdmin):
    list_display = ('nom', 'email', 'telephone', 'adresse', 'ville', 'pays', 'date_commande', 'items', 'total')


class AdminCategoryFoot(admin.ModelAdmin):
    list_display = ('name', 'date_added')


class AdminProductFoot(admin.ModelAdmin):
    list_display = ('titre', 'price', 'category', 'date_added')
    search_fields = ('titre',)
    list_editable = ('price',)


class AdminCommandeFoot(admin.ModelAdmin):
    list_display = (
        'nom', 'email', 'telephone', 'adresse', 'ville', 'pays', 'date_commande',
        'items', 'total')


class AdminCategoryNFL(admin.ModelAdmin):
    list_display = ('name', 'date_added')


class AdminProductNFL(admin.ModelAdmin):
    list_display = ('titre', 'price', 'category', 'date_added')
    search_fields = ('titre',)
    list_editable = ('price',)


class AdminCommandeNFL(admin.ModelAdmin):
    list_display = (
        'nom', 'email', 'telephone', 'adresse', 'ville', 'pays', 'date_commande',
        'items', 'total')


admin.site.register(Registration)
admin.site.register(Category, AdminCategory)
admin.site.register(Product, AdminProduct)
admin.site.register(Commande, AdminCommande)

admin.site.register(CategoryFoot, AdminCategoryFoot)
admin.site.register(ProductFoot, AdminProductFoot)
admin.site.register(CommandeFoot, AdminCommandeFoot)

admin.site.register(CategoryNFL, AdminCategoryNFL)
admin.site.register(ProductNFL, AdminProductNFL)
admin.site.register(CommandeNFL, AdminCommandeNFL)
