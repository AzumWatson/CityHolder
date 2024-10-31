import asyncio
import sys
from bot.launcher import process



async def main():
    await process()


if __name__ == '__main__':
    while True:
        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            print(f"    🤖 See you in the blockchain, crypto captain! Keep those coins rolling! 🚀")
            sys.exit(0)
        except Exception as e:
            print(e)
            sys.exit(0)