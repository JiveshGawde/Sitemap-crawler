import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import CrawlerRunConfig

async def crawl_local_file():
    local_file_path = "cleaned_page.html"  # Replace with your file path
    file_url = f"file://{local_file_path}"
    config = CrawlerRunConfig(bypass_cache=True)

    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=file_url, config=config)
        if result.success:
            print("Markdown Content from Local File:")
            with open("full_extracted2.md", "w", encoding="utf-8") as file:
                file.write(result.markdown)
            print("✅ Markdown saved: full_extracted.md")
        else:
            print(f"Failed to crawl local file: {result.error_message}")

asyncio.run(crawl_local_file())