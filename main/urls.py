from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^user_list/$', user_list, name="user_list"),
    url(r'^user_coffees/(?P<user_id>[0-9]+)/$', user_coffees, name="user_coffees"),
    url(r'^send_order_email/(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})/$', send_order_email, name="send_order_email"),



    url(r'^createCoffee/$', createCoffee, name="createCoffee"),
    url(r'^editCoffee/(?P<coffee_id>[0-9]+)/$', editCoffee, name="editCoffee"),
    url(r'^deleteCoffee/(?P<coffee_id>[0-9]+)/$', deleteCoffee, name="deleteCoffee"),

    url(r'^createBean/$', createBean, name="createBean"),
    url(r'^editBean/(?P<bean_id>[0-9]+)/$', editBean, name="editBean"),
    url(r'^deleteBean/(?P<bean_id>[0-9]+)/$', deleteBean, name="deleteBean"),

    url(r'^createRoast/$', createRoast, name="createRoast"),
    url(r'^editRoast/(?P<roast_id>[0-9]+)/$', editRoast, name="editRoast"),
    url(r'^deleteRoast/(?P<roast_id>[0-9]+)/$', deleteRoast, name="deleteRoast"),

    url(r'^createSyrup/$', createSyrup, name="createSyrup"),
    url(r'^editSyrup/(?P<syrup_id>[0-9]+)/$', editSyrup, name="editSyrup"),
    url(r'^deleteSyrup/(?P<syrup_id>[0-9]+)/$', deleteSyrup, name="deleteSyrup"),

    url(r'^createPowder/$', createPowder, name="createPowder"),
    url(r'^editPowder/(?P<powder_id>[0-9]+)/$', editPowder, name="editPowder"),
    url(r'^deletePowder/(?P<powder_id>[0-9]+)/$', deletePowder, name="deletePowder"),
    url(r'^createOrder/(?P<coffee_id>[0-9]+)/$', createOrder, name="createOrder"),
]
