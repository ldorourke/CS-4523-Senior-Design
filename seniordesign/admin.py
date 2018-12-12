from django.contrib import admin

# Register your models here.
#from .models import User
#admin.site.register(User)


from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .forms import UserAdminChangeForm, UserAdminCreationForm
from .models import UserProfile, CustomUser, EventProfile, uConnectUser
from django.contrib.auth import get_user_model
User = get_user_model()



#Adding the UserProfile Fields to the Django Admin site 
class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


#A more complex view for editing and creating admin
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    inlines = (ProfileInline,)          #inline forms

    def get_inline_instances(self, request, obj=None):          #
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)


    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'admin', 'staff', 'active')
    list_filter = ('admin','staff','active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        #('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin','staff','active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()



# Register your models here.
admin.site.register(CustomUser, UserAdmin)
admin.site.register(EventProfile)

admin.site.register(uConnectUser)
# Unregister your models here. 
admin.site.unregister(Group)       #Not Using this model ... yet?

