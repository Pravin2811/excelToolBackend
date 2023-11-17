#class ProductRouter:
#    excelTool = "excelTool"
#    def db_for_read(self, model, **hints):
#        if model._meta.app_label == 'excel':
#            return self.excelTool
#        return None