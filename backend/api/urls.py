from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AboutViewSet, ExperienceViewSet, ProjectViewSet,
    SkillViewSet, EducationViewSet, ContactInfoViewSet,
    SocialLinkViewSet, AwardViewSet, HobbyViewSet,
    StatisticsViewSet, TestimonialViewSet, SkillAttributeViewSet,
    NavigationItemViewSet, SiteSettingsViewSet
)

router = DefaultRouter()
router.register(r'about', AboutViewSet, basename='about')
router.register(r'experiences', ExperienceViewSet, basename='experience')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'skills', SkillViewSet, basename='skill')
router.register(r'education', EducationViewSet, basename='education')
router.register(r'contact', ContactInfoViewSet, basename='contact')
router.register(r'social-links', SocialLinkViewSet, basename='social-link')
router.register(r'awards', AwardViewSet, basename='award')
router.register(r'hobbies', HobbyViewSet, basename='hobby')
router.register(r'statistics', StatisticsViewSet, basename='statistics')
router.register(r'testimonials', TestimonialViewSet, basename='testimonial')
router.register(r'skill-attributes', SkillAttributeViewSet, basename='skill-attribute')
router.register(r'navigation-items', NavigationItemViewSet, basename='navigation-item')
router.register(r'site-settings', SiteSettingsViewSet, basename='site-settings')

urlpatterns = [
    path('', include(router.urls)),
]

