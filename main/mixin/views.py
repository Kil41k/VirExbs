
class TitleMixin:
    title = 'exhibition'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = self.title
        return context