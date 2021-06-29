from django.contrib import admin
from .models import Generator, Step, Field,FieldData


admin.site.register(Generator)
admin.site.register(FieldData)

@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ('generator', 'name',)
    list_filter = ('generator',)


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('step', 'name', 'field')
    list_filter = ('step',)
