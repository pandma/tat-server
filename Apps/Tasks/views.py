from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Tasks
from ..Subpages.views import Relate_subpages
from rest_framework import generics
import json


class Tasks_views(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        data = list(Tasks.objects.values())
        if len(data) > 0:
            res = {"message": "Success", "data": data}
        else:
            res = {"message": "data not found"}
        return JsonResponse(res)

    def post(self, request):
        jd = json.loads(request.body)
        subpage_id = jd["subpage_id"]
        subpage = Relate_subpages.find_page(self, subpage_id)
        Tasks.objects.create(
            title=jd["title"],
            type=jd["type"],
            text=jd["text"],
            comments=jd["comments"],
            picture_url=jd["picture_url"],
            status=jd["status"],
            subpages=subpage,
        )
        res = {"message": "Success"}
        return JsonResponse(res)

    def put(self, request):
        jd = json.loads(request.body)
        query = jd["id"]
        comp = self.get_by_id(query)
        if len(comp) > 0:
            page = Tasks.objects.get(id=query)
            page.title = (jd["title"],)
            page.type = (jd["type"],)
            page.comments = (jd["comments"],)
            page.picture_url = (jd["picture_url"],)
            page.status = (jd["status"],)
            page.save()
            updated_task = self.get_by_id(query)
            res = {"message": "Success", "data": updated_task}
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
        return list(Tasks.objects.filter(id=id).values())[0]

    def delete_by_id(self, id):
        page = Tasks.objects.get(id=id)
        page.delete()
        return


class One_task_view(generics.ListAPIView):
    def get(self, request):
        id = self.request.GET.get("id", None)
        if id:
            try:
                data = list(Tasks.objects.filter(id=id).values())[0]
                res = {"message": "Success", "data": data}
            except:
                res = {"message": "data not found"}
        else:
            res = {"message": "data not found"}
        return JsonResponse(res)


class Find_by_subpage_id_view(generics.ListAPIView):
    def get(self, request):
        id = self.request.GET.get("id", None)
        if id:
            try:
                data = self.find_by_id(id)
                print(data)
                res = {"message": "Success", "data": data}
            except:
                res = {"message": "data not found"}
        else:
            res = {"message": "data not found"}
        return JsonResponse(res)

    def find_by_id(seld, id):
        return list(Tasks.objects.filter(subpages_id=id).values())
