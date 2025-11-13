from django.contrib import admin
from .models import (
    About, Experience, Project, Skill, Education,
    ContactInfo, SocialLink, Award, Hobby,
    Statistics, Testimonial, SkillAttribute,
    NavigationItem, SiteSettings
)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'tagline', 'show_hero_button', 'show_about_image', 'age', 'website', 'home_country', 'enabled', 'created_at', 'updated_at']
    list_filter = ['enabled', 'show_hero_button', 'show_about_image', 'created_at', 'home_country']
    search_fields = ['name', 'bio', 'tagline', 'website', 'home_country']
    list_editable = ['enabled', 'show_hero_button', 'show_about_image']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'bio', 'profile_image', 'image_shape', 'show_about_image', 'resume')
        }),
        ('Hero Section Configuration', {
            'fields': ('tagline', 'hero_button_text', 'hero_button_link', 'show_hero_button'),
            'description': 'Configure the hero section tagline and action button'
        }),
        ('Personal Details', {
            'fields': ('age', 'website', 'home_country')
        }),
        ('Settings', {
            'fields': ('enabled',)
        }),
    )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'start_date', 'end_date', 'enabled', 'created_at']
    list_filter = ['enabled', 'start_date', 'created_at']
    search_fields = ['title', 'company', 'description']
    list_editable = ['enabled']
    date_hierarchy = 'start_date'


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_shape', 'link', 'enabled', 'created_at']
    list_filter = ['enabled', 'image_shape', 'created_at']
    search_fields = ['title', 'description', 'technologies']
    list_editable = ['enabled']
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'description', 'image', 'image_shape', 'link', 'technologies')
        }),
        ('Settings', {
            'fields': ('enabled',)
        }),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'enabled', 'created_at']
    list_filter = ['enabled', 'category', 'created_at']
    search_fields = ['name', 'category']
    list_editable = ['enabled']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_date', 'end_date', 'enabled', 'created_at']
    list_filter = ['enabled', 'start_date', 'created_at']
    search_fields = ['degree', 'institution', 'description']
    list_editable = ['enabled']
    date_hierarchy = 'start_date'


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone', 'location', 'enabled', 'created_at']
    list_filter = ['enabled', 'created_at']
    search_fields = ['email', 'phone', 'location']
    list_editable = ['enabled']


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['platform', 'url', 'icon', 'enabled', 'created_at']
    list_filter = ['enabled', 'platform', 'created_at']
    search_fields = ['platform', 'url']
    list_editable = ['enabled']


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ['title', 'issuer', 'date', 'enabled', 'created_at']
    list_filter = ['enabled', 'date', 'created_at']
    search_fields = ['title', 'description', 'issuer']
    list_editable = ['enabled']
    date_hierarchy = 'date'


@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'enabled', 'created_at']
    list_filter = ['enabled', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['enabled']


@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ['awards_won', 'happy_customers', 'projects_done', 'games_played', 'enabled', 'updated_at']
    list_filter = ['enabled', 'created_at']
    list_editable = ['enabled']
    fieldsets = (
        ('Statistics', {
            'fields': ('awards_won', 'happy_customers', 'projects_done', 'games_played')
        }),
        ('Settings', {
            'fields': ('enabled',)
        }),
    )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'author_company', 'enabled', 'created_at']
    list_filter = ['enabled', 'created_at']
    search_fields = ['quote', 'author_name', 'author_company']
    list_editable = ['enabled']


@admin.register(SkillAttribute)
class SkillAttributeAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'enabled', 'created_at']
    list_filter = ['enabled', 'created_at']
    search_fields = ['name', 'icon']
    list_editable = ['enabled']


@admin.register(NavigationItem)
class NavigationItemAdmin(admin.ModelAdmin):
    list_display = ['label', 'link', 'is_cta', 'order', 'enabled', 'created_at']
    list_filter = ['enabled', 'is_cta', 'created_at']
    search_fields = ['label', 'link']
    list_editable = ['enabled', 'order', 'is_cta']
    fieldsets = (
        ('Navigation Item', {
            'fields': ('label', 'link', 'is_cta', 'order')
        }),
        ('Settings', {
            'fields': ('enabled',)
        }),
    )


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['enabled', 'updated_at']
    fieldsets = (
        ('Section Titles', {
            'fields': ('about_title', 'skills_title', 'experience_title', 'projects_title', 
                      'education_title', 'awards_title', 'hobbies_title', 'contact_title', 
                      'testimonials_title'),
            'description': 'Customize section titles. Leave empty to use defaults.'
        }),
        ('Footer', {
            'fields': ('footer_text', 'copyright_year'),
            'description': 'Footer text and copyright year. Leave copyright_year empty to use current year.'
        }),
        ('Settings', {
            'fields': ('enabled',)
        }),
    )
    
    def has_add_permission(self, request):
        # Only allow one SiteSettings instance
        return not SiteSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Prevent deletion of SiteSettings
        return False

