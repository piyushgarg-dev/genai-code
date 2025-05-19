import os
import aiofiles


async def save_to_disk(file: bytes, path: str) -> bool:
    os.makedirs(os.path.dirname(path), exist_ok=True)

    async with aiofiles.open(path, "wb") as out_file:
        await out_file.write(file)

    return True
