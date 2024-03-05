from django.contrib.auth import views as auth_views
from django.urls import path
from django_select2 import views as select2_views
from . import views
from .forms import LoginForm

urlpatterns = [
    path('', views.index, name='index'),
    path('api/residents/', views.resident_search, name='resident_search'),
    path('ajax_complainants', views.ajax_complainants, name='ajax_complainants'),
    path('Signup>/', views.Signup, name='Signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout/', views.logout_view, name='logouts'),
    path('brgy_list/', views.brgy_list, name='brgy_list'),
    path('Edit_brgy/', views.Edit_brgy, name='Edit_brgy'),
    path('Delete_brgy/<int:pk>/', views.Delete_brgy, name='Delete_brgy'),
    path('PurokList/', views.PurokList, name='PurokList'),
    path('AdEdPurok/<int:pk>/', views.AdEdPurok, name='AdEdPurok'),
    path('Delete_purok/<int:pk>/', views.Delete_purok, name='Delete_purok'),
    path('ResidentList/', views.ResidentList, name='ResidentList'),
    path('export_residents_to_excel/', views.export_residents_to_excel, name='export_residents_to_excel'),
    path('export_blotter_to_excel/', views.export_blotter_to_excel, name='export_blotter_to_excel'),
    path('Resident/<int:pk>/', views.AdEdResident, name='AdEdResident'),
    path('Users/', views.Users, name='Users'),
    path('AdEdUsers/<int:pk>/', views.AdEdUsers, name='AdEdUsers'),
    path('change_password/', views.change_password, name='change_password'),
    path('Delete_resident/<int:pk>/', views.Delete_resident, name='Delete_resident'),
    path('HouseholdList/', views.HouseholdList, name='HouseholdList'),
    path('AdEdHousehold/<int:pk>/', views.AdEdHousehold, name='AdEdHousehold'),
    path('Delete_household/<int:pk>/', views.Delete_household, name='Delete_household'),
    path('DeceasedList/', views.DeceasedList, name='DeceasedList'),
    path('AdEdDeceased/<int:pk>/', views.AdEdDeceased, name='AdEdDeceased'),
    path('Delete_deceased/<int:pk>/', views.Delete_deceased, name='Delete_deceased'),
    path('OfwList/', views.OfwList, name='OfwList'),
    path('AdEdOfw/<int:pk>/', views.AdEdOfw, name='AdEdOfw'),
    path('Delete_ofw/<int:pk>/', views.Delete_ofw, name='Delete_ofw'),
    path('BlotterList/', views.BlotterList, name='BlotterList'),
    path('AdEdBlotter/<int:pk>/', views.AdEdBlotter, name='AdEdBlotter'),
    path('Delete_blotter/<int:pk>/', views.Delete_blotter, name='Delete_blotter'),
    path('AdEdSummon/<int:pk>/', views.AdEdSummon, name='AdEdSummon'),
    path('SummonList/', views.SummonList, name='SummonList'),
    path('AdEdFileAction/<int:pk>/', views.AdEdFileAction, name='AdEdFileAction'),
    path('FileActionList/', views.FileActionList, name='FileActionList'),

    path('BusinessList/', views.BusinessList, name='BusinessList'),
    path('AdEdBusiness/<int:pk>/', views.AdEdBusiness, name='AdEdBusiness'),
    path('Delete_business/<int:pk>/', views.Delete_business, name='Delete_business'),
    path('JobSeekersList/', views.JobSeekersList, name='JobSeekersList'),
    path('AdEdJobSeekers/<int:pk>/', views.AdEdJobSeekers, name='AdEdJobSeekers'),
    path('Delete_jobseekers/<int:pk>/', views.Delete_jobseekers, name='Delete_jobseekers'),
    path('BrgyClearanceList/', views.BrgyClearanceList, name='BrgyClearanceList'),
    path('AdEdBrgyClearance/<int:pk>/', views.AdEdBrgyClearance, name='AdEdBrgyClearance'),
    path('Delete_brgyclearance/<int:pk>/', views.Delete_brgyclearance, name='Delete_brgyclearance'),
    path('BrgyCertificateList/', views.BrgyCertificateList, name='BrgyCertificateList'),
    path('AdEdBrgyCertificate/<int:pk>/', views.AdEdBrgyCertificate, name='AdEdBrgyCertificate'),
    path('DeathClaimCertificateList/', views.DeathClaimCertificateList, name='DeathClaimCertificateList'),
    path('AdEdDeathClaimCertificate/<int:pk>/', views.AdEdDeathClaimCertificate, name='AdEdDeathClaimCertificate'),
    
    path('Delete_brgycertificate/<int:pk>/', views.Delete_brgycertificate, name='Delete_brgycertificate'),
    path('BusinessClearanceList/', views.BusinessClearanceList, name='BusinessClearanceList'),
    path('AdEdBusinessClearance/<int:pk>/', views.AdEdBusinessClearance, name='AdEdBusinessClearance'),
    path('BusinessCertificateList/', views.BusinessCertificateList, name='BusinessCertificateList'),
    path('AdEdBusinessCertificate/<int:pk>/', views.AdEdBusinessCertificate, name='AdEdBusinessCertificate'),
    
    path('Delete_businessclearance/<int:pk>/', views.Delete_businessclearance, name='Delete_businessclearance'),
    path('CertResidencyList/', views.CertResidencyList, name='CertResidencyList'),
    path('AdEdCertResidency/<int:pk>/', views.AdEdCertResidency, name='AdEdCertResidency'),
    path('Delete_certresidency/<int:pk>/', views.Delete_certresidency, name='Delete_certresidency'),
    path('CertIndigencyList/', views.CertIndigencyList, name='CertIndigencyList'),
    path('AdEdCertIndigency/<int:pk>/', views.AdEdCertIndigency, name='AdEdCertIndigency'),
    path('Delete_certindigency/<int:pk>/', views.Delete_certindigency, name='Delete_certindigency'),
    path('CertSoloParentList/', views.CertSoloParentList, name='CertSoloParentList'),
    path('AdEdCertSoloParent/<int:pk>/', views.AdEdCertSoloParent, name='AdEdCertSoloParent'),
    path('Delete_certsoloparent/<int:pk>/', views.Delete_certsoloparent, name='Delete_certsoloparent'),
    path('CertNonOperationList/', views.CertNonOperationList, name='CertNonOperationList'),
    path('AdEdCertNonOperation/<int:pk>/', views.AdEdCertNonOperation, name='AdEdCertNonOperation'),
    path('Delete_certnonoperation/<int:pk>/', views.Delete_certnonoperation, name='Delete_certnonoperation'),
    path('CertGoodMoralList/', views.CertGoodMoralList, name='CertGoodMoralList'),
    path('AdEdCertGoodMoral/<int:pk>/', views.AdEdCertGoodMoral, name='AdEdCertGoodMoral'),
    path('Delete_certgoodmoral/<int:pk>/', views.Delete_certgoodmoral, name='Delete_certgoodmoral'),
    path('CertTribalList/', views.CertTribalList, name='CertTribalList'),
    path('AdEdTribal/<int:pk>/', views.AdEdTribal, name='AdEdTribal'),
    path('Delete_tribal/<int:pk>/', views.Delete_tribal, name='Delete_tribal'),
    path('AdEdBrgyOfficials/', views.AdEdBrgyOfficials, name='AdEdBrgyOfficials'),
    path('import_residents/', views.import_residents, name='import_residents'),
    path('pdf_report/', views.pdf_report_view, name='pdf_report'),
    
    path('resident_list/', views.pdf_resident_list, name='resident_list'),
    path('pdf_household_list/', views.pdf_household_list, name='pdf_household_list'),
    path('pdf_blotter_list/', views.pdf_blotter_list, name='pdf_blotter_list'),
    path('pdf_ofw_list/', views.pdf_ofw_list, name='pdf_ofw_list'),
    path('pdf_deceased_list/', views.pdf_deceased_list, name='pdf_deceased_list'),
    path('pdf_business_list/', views.pdf_business_list, name='pdf_business_list'),
    path('pdf_JobSeekers_list/', views.pdf_JobSeekers_list, name='pdf_JobSeekers_list'),
    path('pdf_brgyClearance_list/', views.pdf_brgyClearance_list, name='pdf_brgyClearance_list'),
    path('pdf_brgyCertificate_list/', views.pdf_brgyCertificate_list, name='pdf_brgyCertificate_list'),
    path('pdf_deathclaimcert_list/', views.pdf_deathclaimcert_list, name='pdf_deathclaimcert_list'),
    path('pdf_certTribal_list/', views.pdf_certTribal_list, name='pdf_certTribal_list'),
    path('pdf_certNonOperation_list/', views.pdf_certNonOperation_list, name='pdf_certNonOperation_list'),
    path('pdf_certIndigency_list/', views.pdf_certIndigency_list, name='pdf_certIndigency_list'),
    path('pdf_certResidency_list/', views.pdf_certResidency_list, name='pdf_certResidency_list'),
    path('pdf_certGoodMoral_list/', views.pdf_certGoodMoral_list, name='pdf_certGoodMoral_list'),
    path('pdf_certSoloParent_list/', views.pdf_certSoloParent_list, name='pdf_certSoloParent_list'),  
    path('pdf_summon_list/', views.pdf_summon_list, name='pdf_summon_list'),
    path('pdf_FileAction_list/', views.pdf_FileAction_list, name='pdf_FileAction_list'),
    path('pdf_businessClearance_list/', views.pdf_businessClearance_list, name='pdf_businessClearance_list'),
    path('pdf_businessCertificate_list/', views.pdf_businessCertificate_list, name='pdf_businessCertificate_list'),

    path('pdf_JobSeekers/<int:pk>/', views.pdf_JobSeekers, name='pdf_JobSeekers'),
    path('pdf_Oath/<int:pk>/', views.pdf_Oath, name='pdf_Oath'),
    path('pdf_goodmoral/<int:pk>/', views.pdf_goodmoral, name='pdf_goodmoral'),
    path('pdf_residency/<int:pk>/', views.pdf_residency, name='pdf_residency'),
    path('pdf_brgyClearance/<int:pk>/', views.pdf_brgyClearance, name='pdf_brgyClearance'),
    path('pdf_brgyCertificate/<int:pk>/', views.pdf_brgyCertificate, name='pdf_brgyCertificate'),
    path('pdf_deathclaimcert/<int:pk>/', views.pdf_deathclaimcert, name='pdf_deathclaimcert'),
    path('pdf_indigency/<int:pk>/', views.pdf_indigency, name='pdf_indigency'),
    path('pdf_soloparent/<int:pk>/', views.pdf_soloparent, name='pdf_soloparent'),
    path('pdf_tribal/<int:pk>/', views.pdf_tribal, name='pdf_tribal'),
    path('pdf_Summon/<int:pk>/', views.pdf_Summon, name='pdf_Summon'),
    path('pdf_FileAction/<int:pk>/', views.pdf_FileAction, name='pdf_FileAction'),
    path('pdf_businessClearance/<int:pk>/', views.pdf_businessClearance, name='pdf_businessClearance'),
    path('pdf_businessCertificate/<int:pk>/', views.pdf_businessCertificate, name='pdf_businessCertificate'),
    path('pdf_nonOperation/<int:pk>/', views.pdf_nonOperation, name='pdf_nonOperation'),
    path('get_filtered_clearance_data/', views.get_filtered_clearance_data, name='get_filtered_clearance_data'),
    path('get_members/', views.get_members, name='get_members'),
    path('report_body/', views.report_body, name='report_body'),
    path('filter_resident/', views.filter_resident, name='filter_resident'),
    path('SearchResident/', views.SearchResident, name='SearchResident'),
    path('filter-house-no/<int:purok_id>/', views.filter_house_no, name='filter_house_no'),
]