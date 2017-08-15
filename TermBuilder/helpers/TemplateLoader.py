from django.template import loader
from django.shortcuts import redirect

class TemplateLoader():
	
	def loadTemplate(self, template):
	    try:
	        templateToRender = loader.get_template(template)
	        
	    except TemplateDoesNotExist:
	        
	        print("sorry template was not found... ")
	        
	        if template == "home_page.html":
	            return redirect("accounts/login")
	            
	        return redirect("http://127.0.0.1:8000")
	    
	    return templateToRender

	
	