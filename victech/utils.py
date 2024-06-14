import re
from datetime import datetime
from django.db.models import F

from .models import ReportUserBlog


def sanitize_address(address):
	return re.sub(r"\D", "", address)

def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[-1].strip()
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip

def update_or_create_report_user_blog(request):
	address = get_client_ip(request)
	last_path = request.path_info or "Não localizado"
	sanitized_address = sanitize_address(address)

	report_user = ReportUserBlog.objects.filter(address=sanitized_address)

	if report_user:
		now = datetime.now()
		report_user.update(
			last_access_at=now,
			number_of_requests=F('number_of_requests') + 1,
			last_path=last_path,
		)
		return

	ReportUserBlog.objects.create(
		address=sanitized_address,
		number_of_requests=1,
		last_path=last_path,
	)
	return

def replace_partial_text(text, text_find, text_add):
	if not text or not text_find:
		return ''
	text_initial = text[:text.find(text_find)+len(text_find)-1]
	text_final = text[text.find(text_find)+len(text_find)-1:]
	partial = f" id={text_add}"
	return f"{text_initial}{partial}{text_final}"
