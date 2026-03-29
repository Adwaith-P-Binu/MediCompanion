"""pharmacy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index),
    path('first',views.first),
    path('logout/',views.logout),
    path('register/',views.register),
    path('viewuserdoctor',views.viewuserdoctor),
    path('viewuserconsult',views.viewuserconsult),
    path('viewdoctorproduct',views.viewdoctorproduct),
    path('login/',views.login),
    path('productt',views.productt),
    path('addd',views.addd),
    path('adddoctor',views.adddoctor),
    path('viewuserproduct',views.viewuserproduct),
    path('viewdoctorreq',views.viewdoctorreq),
    path('buy/<int:id>',views.buy,name='buy'),
    path('dtt/<int:id>',views.dtt,name='dtt'),
    path('dtt/dconsult',views.dconsult,name='dconsult'),
    path('consult1/<int:id>',views.consult1,name='consult1'),
    path('consult1/addconsult',views.addconsult,name='addconsult'),
    path('buy/paid',views.paid,name='paid'),
    path('register/adduser',views.adduser),
    path('readmin',views.readmin),
    path('requu',views.requu),
    path('addpro/<int:id>',views.addpro,name='addpro'),
    path('addpro/finall',views.finall,name='finall'),
    path('viewuserpaid',views.viewuserpaid),
    path('viewadminpayment',views.viewadminpayment),
    path('login/addlogin',views.addlogin),

    path('login1doc/',views.login1doc),
    path('login1doc/addlogindoc',views.addlogindoc),

    path('login2ph/',views.login2ph),
    path('login2ph/addlogin2ph',views.addlogin2ph),
    
    path('login3user/',views.login3user),
    path('login3user/addlogin3user',views.addlogin3user),
    path('userprescribe',views.userprescribe),
    path('phpres',views.phpres),
    path('adddrug',views.adddrug),
    path('drugdelete/<int:id>',views.drugdelete),
    path('drugupdt/<int:id>',views.drugupdt),
    path('drugupdt/updtdrug/<int:id>',views.updtdrug),
    path('nonmed',views.nonmed),
    path('addnonmed',views.addnonmed),

    path('viewuser/',views.viewuser),
    path('viewdoc',views.viewdoc),
    path('viewph',views.viewph),
    path('docpayssview',views.docpayssview),

    path('deletedoctor/<int:id>',views.deletedoctor,name="deletedoctor"),
    path('updatedoctor/<int:id>',views.updatedoctor,name="updatedoctor"),
    path('updatedoctor/addupdatedoctor/<int:id>',views.addupdatedoctor,name="addupdatedoctor"),
    path('deletepharmacy/<int:id>',views.deletepharmacy,name="deletepharmacy"),
    path('updatepharmacy/<int:id>',views.updatepharmacy,name="updatepharmacy"),
    path('updatepharmacy/addupdatepharmacy/<int:id>',views.addupdatepharmacy,name="addupdatepharmacy"),
    path('update_dosage/<int:id>', views.update_dosage, name='update_dosage'),

    path('phr',views.phr),
    path('addpharmacy',views.addpharmacy),
    path('dosss',views.dosss),
    path('adddosss',views.adddosss),
    path('chatss/<int:id>',views.chatss),
    path('chatss/addchatss',views.addchatss),

    path('paydoc/<int:id>',views.paydoc),
    path('paydoc/addpaydoc',views.addpaydoc),

    path('viewchats',views.viewchats),
    
    path('replyss/<int:id>',views.replyss),
    path('replyss/addreply/<int:id>',views.addreply,name="addreply"),
    path('viewchatsuser',views.viewchatsuser),
    path('viewnoti',views.viewnoti),

    path('useraccept/<int:id>',views.useraccept),
    path('userreject/<int:id>',views.userreject),

    path('viewnotiii',views.viewnotiii),
    path('viewnonusable',views.viewnonusable),
    path('viewchatsall',views.viewchatsall),
    path('forget/',views.forget),
    path('forget/forgetpassword',views.forgetpassword),
    path('feed/',views.feed),
    path('feed/addfeed',views.addfeed),
    path('viewfeed',views.viewfeed),
    path('gello',views.gello),
    path('admin/', admin.site.urls),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
