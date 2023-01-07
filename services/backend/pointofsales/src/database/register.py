from typing import Optional

from tortoise import Tortoise


def register_tortoise(
    app,
    config: Optional[dict] = None,
    generate_schemas: bool = False,
) -> None:
    """_summary_

    Args:
        app (_type_): _description_
        config (Optional[dict], optional): _description_. Defaults to None.
        generate_schemas (bool, optional): _description_. Defaults to False.
    """
    @app.on_event("startup")
    async def init_orm():
        await Tortoise.init(config=config)
        if generate_schemas:
            await Tortoise.generate_schemas()

    @app.on_event("shutdown")
    async def close_orm():
        await Tortoise.close_connections()
