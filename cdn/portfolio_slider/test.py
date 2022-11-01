import glob

txtfiles = []
for file in glob.glob("*.png"):
    txtfiles.append(file)
for file in txtfiles:
    print("""

            <div class="swiper-slide swiper-slider">
              <img src="/cdn/portfolio_slider/%s" alt="%s" />
            </div>
""" %(file,file))
