import json
import asyncio


from ubc import db


async def main():
    await db.setup_database()
    reticle = db.Reticle(name="ubc1")
    # foundry = db.Foundry(name="ANT")
    # foundry_process = db.FoundryProcess(name="passives", foundry=foundry)
    # lot = db.Lot(name="lot1", foundry_process=foundry_process, reticle=reticle)
    # wafer = db.Wafer(name="wafer1", lot=lot)
    # die = db.Die(name="die1", wafer=wafer)

    settings = json.dumps(dict(length=10, width=0.5))
    component_model = db.Component(name="straight", settings=settings, reticle=reticle)
    await component_model.save()

    # instance = db.Instance(
    #     component=component_model,
    #     x=component.label.x,
    #     y=component.label.y,
    # )
    # await instance.save()

    # measurement_x = [0, 1, 2]
    # measurement_y = [0, 2, 4]
    # measurement = db.Measurement()

    # all_instances = await db.Instance.all()
    # print(all_instances)


if __name__ == "__main__":
    asyncio.run(main())
