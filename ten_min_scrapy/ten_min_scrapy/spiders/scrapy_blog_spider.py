import scrapy
from ten_min_scrapy.items import Post

class ScrapyBlogSpiderSpider(scrapy.Spider):
    name = 'scrapy_blog_spider'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['http://blog.scrapinghub.com/']

    def parse(self, response):

        # レスポンスに対するパース処理
        # response.css でscrapyデフォルトのcssセレクタを利用できる
        for post in response.css ('.post-listening .post-items'):
            # itemsに定義したPostのオブジェクト生成して次の処理へ渡す
            yield Post (
                url = post.css ('div.post-header a::attr(href)').extract_first().strip(),
                title = post.css ('div.post-header a::text').extract_first().strip(),
                date = post.css ('div.post-header span.date a::text').extract_first().strip(),
            )

        # 再帰的にページングを辿るための処理
        older_post_link = response.css('').extract_first()
        if older_post_link is None :
            # リンクが取得できなかった場合は最後のページなので処理を終了
            return

        # URLが相対パスだった場合に絶対パスに変換する
        older_post_link = response.urljoin(older_post_link)
        # 次のページのリクエストを実行する
        yield scrapy.Request(older_post_link, callbak = self.parse)
        pass
