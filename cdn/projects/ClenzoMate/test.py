import glob

txtfiles = []
for file in glob.glob("*"):
    txtfiles.append(file)
for file in txtfiles:
    print("""
<div class="col-lg-4 col-md-6 portfolio-item ">
<a href="/cdn/projects/ClenzoMate/%s" data-gallery="portfolioGallery" class="portfolio-lightbox preview-link" title="%s">
<img src="/cdn/projects/ClenzoMate/%s" class="img-fluid" alt="%s"/>
</a></div>""" %(file,file,file,file))
