from django.urls import reverse
from .test_work_base import WorkTestsBase
# Create your tests here.


class URLTemplateTests(WorkTestsBase):
    def test_home_view_loads_template_OK(self):
        response = self.client.get(reverse('my_app:index-page'))
        self.assertTemplateUsed(response, 'my_app/index.html')

    def test_login_view_loads_template_OK(self):
        self.make_user()
        response = self.client.get(reverse('my_app:login-page'))
        self.assertTemplateUsed(response, 'my_app/index.html')

    def test_success_view_loads_template_OK(self):
        response = self.client.get(reverse('my_app:success-page'))
        self.assertTemplateUsed(response, 'my_app/success.html')

    def test_success_account_view_loads_template_OK(self):
        response = self.client.get(reverse('my_app:success-account-page'))
        self.assertTemplateUsed(response, 'my_app/success_account.html')

    def test_signup_view_loads_template_OK(self):
        response = self.client.get(reverse('my_app:signup-page'))
        self.assertTemplateUsed(response, 'my_app/signup.html')

    def test_work_view_loads_template_OK(self):
        response = self.client.get(reverse('my_app:work-page'))
        self.assertTemplateUsed(response, 'my_app/work/work.html')

    def test_work_construction_view_loads_template_OK(self):
        response = self.client.get(reverse('my_app:work-construction-page'))
        self.assertTemplateUsed(response, 'my_app/work/work_construction.html')

    def test_work_construction_form_view_loads_template_OK(self):
        self.make_user()
        response = self.client.get(reverse('my_app:work-construction-form-page'))
        self.assertTemplateUsed(response, 'my_app/work/work_form.html')

    def test_work_cleaning_view_loads_template_OK(self):
        response = self.client.get(reverse('my_app:work-cleaning-page'))
        self.assertTemplateUsed(response, 'my_app/work/work_cleaning.html')

    def test_work_cleaning_form_view_loads_template_OK(self):
        self.make_user()
        response = self.client.get(reverse('my_app:work-cleaning-form-page'))
        self.assertTemplateUsed(response, 'my_app/work/work_form.html')

    def test_work_other_view_loads_template_OK(self):
        response = self.client.get(reverse('my_app:work-other-page'))
        self.assertTemplateUsed(response, 'my_app/work/work_others.html')

    def test_work_other_form_view_loads_template_OK(self):
        self.make_user()
        response = self.client.get(reverse('my_app:work-other-form-page'))
        self.assertTemplateUsed(response, 'my_app/work/work_form.html')

    def test_service_view_loads_template_OK(self):
        response = self.client.get(reverse('my_app:service-page'))
        self.assertTemplateUsed(response, 'my_app/service/service.html')

    def test_service_form_view_loads_template_OK(self):
        self.make_user()
        response = self.client.get(reverse('my_app:service-form-page'))
        self.assertTemplateUsed(response, 'my_app/service/service_form.html')

    def test_service_domestic_view_loads_template_OK(self):
        response = self.client.get(reverse('my_app:service-domestic-page'))
        self.assertTemplateUsed(response, 'my_app/service/service.html')

    def test_service_healthy_beauty_view_loads_template_OK(self):
        response = self.client.get(reverse('my_app:service-healthy-beauty-page'))
        self.assertTemplateUsed(response, 'my_app/service/service.html')

    def test_service_transport_view_loads_template_OK(self):
        response = self.client.get(reverse('my_app:service-transport-page'))
        self.assertTemplateUsed(response, 'my_app/service/service.html')

    def test_service_food_view_loads_template_OK(self):
        response = self.client.get(reverse('my_app:service-food-page'))
        self.assertTemplateUsed(response, 'my_app/service/service.html')

    def test_service_technic_view_loads_template_OK(self):
        response = self.client.get(reverse('my_app:service-technic-page'))
        self.assertTemplateUsed(response, 'my_app/service/service.html')

    def test_service_other_view_loads_template_OK(self):
        response = self.client.get(reverse('my_app:service-other-page'))
        self.assertTemplateUsed(response, 'my_app/service/service.html')
