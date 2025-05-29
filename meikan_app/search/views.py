from django.shortcuts import render, get_object_or_404
from django.views import View
from django.db.models import Q
import csv
from django.http import HttpResponse

from .forms import MemberForm
from .models import Member


# トップページ
class IndexView(View):
    def get(self, request):
        return render(request, "search/index.html")


# 検索、一覧
class SearchMainView(View):
    # 初期表示
    def get(self, request):
        if not request.GET:
            form = MemberForm()
            # 全件取得して10件表示する
            member_list = Member.objects.all()[:10]
        else:
            form = MemberForm(request.GET)
            member_list = []

            # 詳細画面から戻りの場合
            if form.is_valid():
                search_param = form.cleaned_data
                company = search_param.get("company")
                name = search_param.get("name")

                # 検索条件の指定
                filter_conditions = util.create_param(
                    ("company", company), ("name", name)
                )
                member_list = Member.objects.filter(filter_conditions)

        return render(
            request,
            "search/search_main.html",
            {"form": form, "member_list": member_list},
        )

    # 検索処理
    def post(self, request):
        form = MemberForm(request.POST)
        member_list = []

        # 入力チェック
        if form.is_valid():
            # フォームのデータをそのまま取得
            search_param = form.cleaned_data
            company = search_param.get("company")
            name = search_param.get("name")

            # 検索条件の指定
            filter_conditions = util.create_param(("company", company), ("name", name))
            member_list = Member.objects.filter(filter_conditions)

        return render(
            request,
            "search/search_main.html",
            {"form": form, "member_list": member_list},
        )


# ダウンロード
class SelectedDownloadView(View):
    def post(self, request):
        # POSTされたmember.idを取得
        selected_ids = request.POST.getlist("selected_members")

        members = Member.objects.filter(id__in=selected_ids)

        # CSV出力
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="selected_members.csv"'

        # ヘッダー指定
        writer = csv.writer(response)
        writer.writerow(["所属", "名前", "誕生日", "出身", "経歴", "受賞歴"])

        # 選択した分を繰り返す
        for member in members:
            writer.writerow(
                [
                    member.company,
                    member.name,
                    member.birthday,
                    member.hometown,
                    member.history,
                    member.awards,
                ]
            )

        return response


# 詳細
class SearchDetailView(View):
    def get(self, request, id):
        member = get_object_or_404(Member, id=id)

        company = request.GET.get("company", "")
        name = request.GET.get("name", "")

        return render(
            request,
            "search/search_detail.html",
            {"member": member, "company": company, "name": name},
        )


# ユーティリティクラス
class util:
    # パラメータの作成
    def create_param(company, name):
        conditions = Q()

        key1, value1 = company
        if value1 != "":
            conditions &= Q(**{key1 + "__icontains": value1})  # 部分一致でも
        key2, value2 = name
        if value2 != "":
            conditions &= Q(**{key2 + "__icontains": value2})  # 部分一致でも

        return conditions


index = IndexView.as_view()
search_main = SearchMainView.as_view()
selected_download = SelectedDownloadView.as_view()
search_detail = SearchDetailView.as_view()
