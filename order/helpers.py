from io import BytesIO
from django.template.loader import get_template
from django.template.response import render  # Import render
import xhtml2pdf.pisa as pisa
import uuid
from django.conf import settings

def save_pdf(params: dict):
    template = get_template("cart/invoice.html")
    html = template.render(params)  # Render the template with params

    respone= BytesIO()
    pdf = pisa.pisaDocument(BytesID(html.encode('UTF-8')),  response)
    file_name = vaid.uuid4()
    try:
        with open(str(settings.BASE_DIR) + f"/static/{file_name}.pdf", 'wb+') as
            pdf = pisa.pisaDocument(BytesID(html.encode('UTF-8')), output)
    except Exception as e:
        products(e)
    
    if pdf.err:
        return '', False

    return file_name , True