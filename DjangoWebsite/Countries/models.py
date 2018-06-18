from django.db import models

# Create your models here.

class countries(models.Model):
    country_name = models.CharField(max_length=200, null=True)
    population = models.IntegerField(verbose_name="Population")
    languages = models.CharField(max_length=200, null=True)

    def __str__(self):
        lstAtt = [self.country_name, self.population, self.languages]
        return str(lstAtt)
        # return self.country_name
    
    # def getAllAttribute(self):
    #     lstAtt = [self.country_name, self.population, self.languages]
    #     return lstAtt


class pop(models.Model):
    c_pop = models.ForeignKey(countries, on_delete=models.CASCADE)
    accessed = models.CharField(max_length=200, null=True)
    selected_country_language = countries.languages
    selected_country_population = countries.population

    def __str__(self):
        return self.accessed
