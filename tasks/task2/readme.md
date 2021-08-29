## Tasks 2

As a transportation company user, I want to be able to save, delete, get information about the Trucks and Drivers I have.
 

So, the task is:

- To have a hardcoded list of dictionaries that have trucks information like: plate, type, color and other things you can think they can have
- To have the following endpoints for Trucks
    - get all ➡️ GET
    - get by id ➡️ GET
    - save ➡️ POST
    - delete by id ➡️ DELETE
- To have a hardcoded list of dictionaries that have drivers information like: id, name, last_name, license_number, trunck_id and other things you can think they can have
- To have the following endpoints for Drivers
    - get all ➡️ GET
    - get by id ➡️ GET
    - save ➡️ POST
    - delete by id ➡️ DELETE
    - get the information about the truck of a driver ➡️ GET /api/v1/driver/driver_name_or_driver_id/truck