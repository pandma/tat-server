from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Pages
import json
from rest_framework import generics


class Pages_views(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        data = list(Pages.objects.values())
        if len(data) > 0:
            res = {"message": "Success", "data": data}
        else:
            res = {"message": "data not found"}

        return JsonResponse(res)

    def post(self, request):
        jd = json.loads((request.body))
        Pages.objects.create(
            title=jd["title"],
            big_image=jd["big_image"],
            small_image=jd["small_image"],
        )
        res = {"message": "Success"}
        return JsonResponse(res)

    def put(self, request):
        jd = json.loads(request.body)
        query = jd["id"]
        comp = self.get_by_id(query)
        if len(comp) > 0:
            page = Pages.objects.get(id=query)
            page.title = jd["title"]
            page.big_image = jd["big_image"]
            page.small_image = jd["small_image"]
            page.save()
            updated_page = self.get_by_id(query)

            res = {"message": "Success", "data": updated_page}
        else:
            res = {"message": "data not found"}
        return JsonResponse(res)

    def delete(self, request):
        jd = json.loads(request.body)
        query = jd["id"]
        self.delete_by_id(query)
        res = {"message": "deleted susccesfull"}
        return JsonResponse(res)

    def get_by_id(self, id):
        return list(Pages.objects.filter(id=id).values())[0]

    def delete_by_id(self, id):
        page = Pages.objects.get(id=id)
        page.delete()
        return


class Relate_pages:
    def find_page(self, page_id):
        return list(Pages.objects.filter(id=page_id))[0]


class One_page_views(generics.ListAPIView):
    def get(self, request):
        id = self.request.GET.get("id", None)
        if id:
            try:
                data = list(Pages.objects.filter(id=id).values())[0]
                res = {"message": "Success", "data": data}
            except:
                res = {"message": "data not found"}
        else:
            res = {"message": "data not found"}
        return JsonResponse(res)
