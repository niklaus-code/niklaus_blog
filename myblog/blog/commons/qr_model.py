import qrcode


class qr(object):

    def __init__(self):
        self.img_path = "/var/www/mysite/html/static/img/qr_img/qr_"
        self.img_url = "https://manyushuai.site/blog/blog_info?"

    def make_pic(self, id, signature):
        try:
            img = self.img_path + str(id) + ".png"
            url = self.img_url+"id="+str(id)+"&signature="+signature
            qr_code = qrcode.make(url)
            qr_code.save(img)
        except:
            return False

c = qr()
c.make_pic(1310, '9d276981b98e79a02483bd6d4bc28fbe')
