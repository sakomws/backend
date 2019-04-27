from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from utils.error_codes import ResponseCodes
from utils.generic_json_creator import create_response
from django.http import JsonResponse
from jobapps.models import JobApplication, SourceType
from company.models import Company
from position.models import JobPosition
from users.models import EmploymentAuth, EmploymentStatus
from .serializers import ReviewSerializer
from .models import Review, CompanyEmploymentAuth


@csrf_exempt
@api_view(["POST"])
def add_or_update_review(request):    
    body = request.data
    user = request.user
    if 'job_app_id' not in body or 'company_id' not in body or 'position_id' not in body:
        return JsonResponse(create_response(None, False, ResponseCodes.invalid_parameters), safe=False)
    job_app = JobApplication.objects.get(pk=body['job_app_id']) 
    company = Company.objects.get(pk=body['company_id'])  
    position = JobPosition.objects.get(pk=body['position_id'])
    if job_app.user.pk != user.pk:
        return JsonResponse(create_response(None, False, ResponseCodes.record_not_found), safe=False)
    if job_app.position.id != position.id or job_app.companyObject.id != company.id:
        return JsonResponse(create_response(None, False, ResponseCodes.record_not_found), safe=False)    
    if 'review_id' in body:
        review = Review.objects.get(pk=body['review_id']) 
        if review.jobapp.user.pk != user.pk:
            return JsonResponse(create_response(None, False, ResponseCodes.record_not_found), safe=False)
    else:       
        review = Review()
    review.company = company
    review.position = position
    review.jobapp = job_app
    if 'pros' in body:
        review.pros = body['pros']
    if 'cons' in body:
        review.cons = body['cons']
    if 'interview_notes' in body:
        review.interview_notes = body['interview_notes']
    if 'overall_company_experience' in body:
        review.overall_company_experience = body['overall_company_experience']
    if 'interview_difficulty' in body:
        review.interview_difficulty = body['interview_difficulty']    
    if 'overall_interview_experience' in body:
        review.overall_interview_experience = body['overall_interview_experience']
    if 'anonymous' in body:
        review.anonymous = body['anonymous']    
    if 'emp_auths' in body:
        for a in body['emp_auths']:
            if 'value' in a:
                auth = EmploymentAuth.objects.get(pk=a['id'])
                if CompanyEmploymentAuth.objects.filter(review=review, employment_auth=auth).count() == 0:
                    CompanyEmploymentAuth.objects.create(review=review, employment_auth=auth, value=a['value']) 
                else:
                    c_auth =CompanyEmploymentAuth.objects.get(review=review, employment_auth=auth)
                    c_auth.value = a['value']  
                    c_auth.save()
    if 'emp_status_id' in body:
        review.emp_status = EmploymentStatus.objects.get(pk=body['emp_status_id'])   
    if 'source_type_id' in body:
        review.source_type = SourceType.objects.get(pk=body['source_type_id'])       

    review.save()
    return JsonResponse(create_response(ReviewSerializer(instance=review, many=False).data), safe=False) 

@csrf_exempt
@api_view(["GET"])
def get_reviews(request):
    company_id = request.GET.get('company_id')
    position_id = request.GET.get('position_id')
    if company_id is None and position_id is None:
        return JsonResponse(create_response(None, False, ResponseCodes.invalid_parameters), safe=False)
    if company_id is None:
        reviews = Review.objects.filter(position__pk=position_id)
    elif position_id is None:
        reviews = Review.objects.filter(company__pk=company_id)    
    else:
        reviews = Review.objects.filter(position__pk=position_id, company__pk=company_id)    
    return JsonResponse(create_response(ReviewSerializer(instance=reviews, many=True).data), safe=False)           