import glob

txtfiles = []
for file in glob.glob("*"):
    txtfiles.append(file)
for file in txtfiles:
    print("""
<div class="col-lg-4 col-md-6 portfolio-item ">
<a href="/cdn/projects/Fat Prince_Second Prior List/portfolio/%s" data-gallery="portfolioGallery" class="portfolio-lightbox preview-link" title="%s">
<img src="/cdn/projects/Fat Prince_Second Prior List/portfolio/%s" class="img-fluid" alt=""/>
</a></div>""" %(file,file,file))
