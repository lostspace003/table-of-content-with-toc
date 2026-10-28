import os, sys, asyncio, certifi
BUNDLE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'combined-ca.pem')
certifi.where = lambda: BUNDLE
os.environ['SSL_CERT_FILE'] = BUNDLE
import edge_tts
async def main(text, out, voice):
    c = edge_tts.Communicate(text, voice, proxy=os.environ.get('HTTPS_PROXY'), rate='-3%')
    await c.save(out)
if __name__ == '__main__':
    asyncio.run(main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv)>3 else 'en-US-AndrewNeural'))
