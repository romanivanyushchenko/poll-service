from django.contrib import admin

from api_app.models import PollModel, QuestionModel, AnswerModel


class PollModelAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['start_date']
        return []


class QuestionModelAdmin(admin.ModelAdmin):
    pass


class AnswerModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(PollModel, PollModelAdmin)
admin.site.register(QuestionModel, QuestionModelAdmin)
admin.site.register(AnswerModel, AnswerModelAdmin)
