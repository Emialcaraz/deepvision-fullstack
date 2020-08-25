# Event JSON schema

This schema used by Vehicle AI module to report traffic events is the following:

```
{
    "timestamp": str,
    "module": str,
    "module_version": str,
    "json_version": str,
    "module_id": str,
    "camera_uuid": str,
    "events":[
        {
            "uuid": str,
            "instance": str,
            "images":[
                {
                    "timestamp": str,
                    "path": Optional[str],
                    "file": Optional[str],
                    "filename": Optional[str],
                    "encoding": Optional[str]
                }
            ],
            "trajectory":{
                "coordinates":[
                    {
                        "timestamp": str,
                        "x": float,
                        "y": float,
                        "w": float,
                        "h": float
                    }
                ],
                "checkpoints":[
                    {
                        "uuid": str,
                        "timestamp": str,
                        "checkpoint_type": str,
                        "checkpoint_name": str,
                        "direction": str
                    }
                ]
            },
            "alerts": [
                {
                    "timestamp": str,
                    "type": str,
                    "name": str,
                    "details": dict
                }
            ],
            "attributes":[
                {
                    "name": str,
                    "type": str,
                    "format": str,
                    "value": str || int || float || list || dict,
                    "score": float
                }
            ]
        }
    ]
}
```

## To solve the challenge we only need to know about the following fields.

- [timestamp](#timestamp)
  
- [camera_uuid](#camerauuid)

- [events](#events)

  - [uuid](#uuid)

  - [instance](#instance)

  - [trajectory](#trajectory)

    - [checkpoints](#checkpoints)

  - [alerts](#alerts)sc

### timestamp

The last timestamp where the object was tracked.
Expected format: [ISO 8601](https://es.wikipedia.org/wiki/ISO_8601)

- Type: `string`
- Example: `2020-04-14T20:30:59.191515+00:00`

### camera_uuid

The camera ID that tracked the object.

- Type: `string`
- Example: `a46e9ff9-6c53-5eb0-90b3-4e987b309d92`

### events

This field consists in a list of events. Every frame the AI module check for all tracking objects (from now called tracklets),
and if there are some that were missing, sends the JSON with the list of tracked objects.

- Type: `list`
- Schema:
```
    {
        "uuid": str,
        "instance": str,
        "images":[],
        "trajectory":{
            "coordinates":[
                {
                    "timestamp": str,
                    "x": float,
                    "y": float,
                    "h": float,
                    "w": float
                }
            ],
            "checkpoints":[
                {
                    "uuid": str,
                    "timestamp": str,
                    "checkpoint_type": str,
                    "checkpoint_name": str,
                    "direction": str
                }
            ]
        },
        "alerts": [
            {
                "timestamp": str,
                "type": str,
                "name": str,
                "details": dict
            }
        ],
        "attributes":[
            {
                "name": str,
                "type": str,
                "format": str,
                "value": str || int || float || list || dict,
                "score": float
            }__
        ]
    }
```

The only fields that we need to know to solve the challenge are described below.

### uuid

The event UUID represents the tracklet UUID. This is an UUID4.

- Type: `string`
- Example: `1d4742b5-8461-4ba7-8283-0ec709ccb414`

### instance

The instance refers to object type detected.

- Type: `string`
- Example: `person`

It must be one of the following.
- person
- car
- bus
- truck
- motorbike
- bicycle

### trajectory

It is an object that contains all the information related to the trajectory and the checkpoints crossed by the tracklet.

- Type: `dict`
- Schema:
```
    {
        "coordinates": [
            {
                "timestamp": str,
                "x": float,
                "y": float,
                "h": float,
                "w": float
            }
        ],
        "checkpoints": [
            {
                "uuid": str,
                "timestamp": str,
                "checkpoint_type": str,
                "checkpoint_name": str,
                "direction": str
            }
        ]
    }
```

#### checkpoints

It is a list of checkpoints that the tracklet passed through.

- Type: `list`
- Schema:
```
    [
        {
            "uuid": str,
            "timestamp": str,
            "checkpoint_type": str,
            "checkpoint_name": str,
            "direction": str
        }
    ]
```

  **`uuid:`** the UUID4 that uniquely identifies the checkpoint.

  **`timestamp:`** the timestamp when it happened. It must be in isoformat.

  **`checkpoint_type:`** it must be one of the following types:
  - line 
  - zone 

  **`checkpoint_name:`** the checkpoint name.

  **`direction:`** indicates the direction in which the tracklet crossed the checkpoint. It must be one of the following values:
  - in 
  - out 

### alerts

It is a list of alerts.

- Type: `list`
- Schema:
```
    [
        {
            "timestamp": str,
            "type": str,
            "name": str,
            "details": dict,
        }
    ]
```
  **`timestamp:`** the timestamp when the alert was triggered. It must be in UTC isoformat.

  **`type:`** for traffic events must be **trafficAnomaly**.

  **`name:`** the alert name must be one of the following values:
  
  - jaywalking 
  - wrongWay 
  - queueClearing 
  - unsafeLaneEntry 
  - stalledCar 
  - trafficCongestion 
  - illegalTurn 

  **`details:`** Only the **trafficCongestion** anomaly must specify this field according the following struct:

```
"details": {
    "congestion_uuid": "1d4742b5-8461-4ba7-8283-0ec709ccb494",
    "zone_uuid": "dfeb89c7-5831-4c82-ab18-221345061d7e"
}
```

- Example:

One *tracklet* might be involved in one or more anomalies. Below an example of the alerts field:

- Alerts:
```
    [
        {
                "timestamp": "2020-06-26T17:20:51.000Z",
                "type": "trafficAnomaly",
                "name": "wrongWay",
        },
        {
                "timestamp": "2020-06-26T17:22:50.000Z",
                "type": "trafficAnomaly",
                "name": "trafficCongestion",
                "details": {
                    "congestion_uuid": "1d4742b5-8461-4ba7-8283-0ec709ccb494",
                    "zone_uuid": "dfeb89c7-5831-4c82-ab18-221345061d7e"
                }
        },
        {
                "timestamp": "2020-06-26T17:30:53.000Z",
                "type": "trafficAnomaly",
                "name": "trafficCongestion",
                "details": {
                    "congestion_uuid": "1d4742b5-8461-4ba7-8283-0ec709ccb494",
                    "zone_uuid": "dfeb89c7-5831-4c82-ab18-221345061d7e"
                }
        },
        {
                "timestamp": "2020-06-26T17:32:54.000Z",
                "type": "trafficAnomaly",
                "name": "unsafeLaneEntry",
        }
    ]
```
