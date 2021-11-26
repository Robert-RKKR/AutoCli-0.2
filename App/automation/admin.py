# Django Import:
from django.contrib import admin

# Application Import:
from .models.automation_policy import *
from .models.relations import *
from .models.task_manager import *
from .models.template import *

# Register your models here.
admin.site.register(Template)
admin.site.register(AutomationPolicy)
admin.site.register(TaskManager)
admin.site.register(TemplateAutomationPolicyRelation)
admin.site.register(DeviceAutomationPolicyRelation)
admin.site.register(GroupAutomationPolicyRelation)