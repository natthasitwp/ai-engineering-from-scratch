import logging
import anthropic

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

client = anthropic.Anthropic()

try:
    response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=256,
        messages=[{"role": "user", "content": "What is a neural network in one sentence?"}],
    )
    logger.info("SDK response: %s", response.content[0].text)
    logger.info("Tokens: %d in, %d out",
                response.usage.input_tokens, response.usage.output_tokens)

except anthropic.RateLimitError:
    logger.warning("Rate limited, retry later")
except anthropic.APIStatusError as e:
    logger.error("API error %s: %s", e.status_code, e.message)
except Exception:
    logger.exception("Unexpected error")  # พิมพ์ traceback ให้อัตโนมัติ