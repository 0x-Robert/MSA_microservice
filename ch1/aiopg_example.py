import asyncio
import aiopg 

#asyncio를 사용한 또 다른 프로젝트인 aiopg는 PostgreSQL용 라이브러리다. 
#다음은 aiopg의 공식문서에서 가져온 예제코드다.

dsn= 'dbname=aiopg user=aiopg password=passwd host=127.0.0.1'

async def go():
    pool = await aiopg.create_pool(dsn)
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT 1")
            ret = []
            async for row in cur:
                ret.append(row)
            assert ret == [(1,)]
loop=asyncio.get_event_loop()
loop.run_until_complete(go())


