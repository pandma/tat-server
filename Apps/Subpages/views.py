from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Subpages
from ..Pages.views import Relate_pages
import json


class Subpages_views(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        data = list(Subpages.objects.values())
        if len(data) > 0:
            res = {"message": "Success", "data": data}
        else:
            res = {"message": "data not found"}
        return JsonResponse(res)

    def post(self, request):
        jd = json.loads((request.body))
        page_id = jd["page_id"]
        page = Relate_pages.find_page(self, page_id)

        Subpages.objects.create(
            title=jd["title"],
            big_image=jd["big_image"],
            small_image=jd["small_image"],
            pages=page,
        )
        res = {"message": "Success"}
        return JsonResponse(res)

    def put(self, request):
        jd = json.loads(request.body)
        query = jd["id"]
        comp = self.get_by_id(query)
        if len(comp) > 0:
            page = Subpages.objects.get(id=query)
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
        return list(Subpages.objects.filter(id=id).values())[0]

    def delete_by_id(self, id):
        page = Subpages.objects.get(id=id)
        page.delete()
        return


class Relate_subpages:
    def find_page(self, Subpages_id):
        return list(Subpages.objects.filter(id=Subpages_id))[0]
