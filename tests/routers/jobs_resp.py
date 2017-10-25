success = {
    "uuid": "8bf7e570-67cd-4670-a37c-0999fd07f9bf",
    "action": "JobsRouter",
    "result": {
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "detail"
}

fail = {
    "uuid": "e165fbec-d5e9-43a6-95dc-a6f4e73c51ad",
    "action": "JobsRouter",
    "result": {
        "msg": "NoSuchJobException: 9ba5c8d7-58de-4f18-96fe-d362841910dd",
        "type": "exception",
        "success": False
    },
    "tid": 1,
    "type": "rpc",
    "method": "getInfo"
}

get_jobs = {
    "uuid": "d4d01c9a-b299-44b7-97a3-ff96e9bcbd06",
    "action": "JobsRouter",
    "result": {
        "totalCount": 585,
        "jobs": [
            {
                "scheduled": 1508784433,
                "status": "PENDING",
                "description": "Create test2.example.com under /Server/TEST",
                "started": None,
                "finished": None,
                "user": "zenoss",
                "uid": "/zport/dmd/JobManager",
                "type": "Create Device",
                "uuid": "721739ae-2b1d-4613-91e9-681f134a2c49"
            },
            {
                "scheduled": 1508527259,
                "status": "FAILURE",
                "description": "Discover and model device test.example.com as /Server/TEST",
                "started": 1508527358,
                "finished": 1508527405,
                "user": "zenoss",
                "uid": "/zport/dmd/JobManager",
                "type": "Shell Command",
                "uuid": "9ba5c8d7-58de-4f18-96fe-d362841910d3"
            }
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getJobs"
}

job1 = {
    "uuid": "0a39a730-9d41-48fb-878e-a5cbbbc1116a",
    "action": "JobsRouter",
    "result": {
        "data": {
            "scheduled": 1508784433,
            "status": "PENDING",
            "errors": "",
            "description": "Create test2.example.com under /Server/TEST",
            "started": None,
            "uuid": "721739ae-2b1d-4613-91e9-681f134a2c49",
            "name": "JobManager",
            "duration": None,
            "finished": None,
            "meta_type": "Object Manager",
            "user": "zenoss",
            "inspector_type": "Object Manager",
            "logfile": None,
            "type": "Create Device",
            "id": "721739ae-2b1d-4613-91e9-681f134a2c49",
            "uid": "/zport/dmd/JobManager"
        },
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getInfo"
}

job2 = {
    "uuid": "a5b44931-d5e1-48cf-8084-cb304d814ffe",
    "action": "JobsRouter",
    "result": {
        "data": {
            "scheduled": 1508527259,
            "status": "FAILURE",
            "errors": "2017-10-20 19:21:52,042 ERROR zen.SshClient: 10.0.3.30 User timeout caused connection failure.\n",
            "description": "Discover and model device test.example.com as /Server/TEST",
            "started": 1508527358,
            "uuid": "9ba5c8d7-58de-4f18-96fe-d362841910d3",
            "name": "JobManager",
            "duration": 47,
            "finished": 1508527405,
            "meta_type": "Object Manager",
            "user": "zenoss",
            "inspector_type": "Object Manager",
            "logfile": "/opt/zenoss/log/jobs/9ba5c8d7-58de-4f18-96fe-d362841910d3.log",
            "type": "Shell Command",
            "id": "9ba5c8d7-58de-4f18-96fe-d362841910d3",
            "uid": "/zport/dmd/JobManager"
        },
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getInfo"
}

detail = {
    "uuid": "28ea704d-509e-4654-b87c-182ecd30579b",
    "action": "JobsRouter",
    "result": {
        "content": [
            "2017-10-20 19:22:38,949 INFO zen.Job: Job 9ba5c8d7-58de-4f18-96fe-d362841910d3 (Products.Jobber.jobs.SubprocessJob) received\n",
            "2017-10-20 19:22:39,158 INFO zen.Job: Starting job 9ba5c8d7-58de-4f18-96fe-d362841910d3 (Products.Jobber.jobs.SubprocessJob)\n",
            "2017-10-20 19:22:39,158 INFO zen.Job: Spawning subprocess: zminion -minion-name zminion_auw2collector run -- /opt/zenoss/bin/zendisc run --now -d test.example.com --monitor localhost --deviceclass /Server/TEST --prod_state 900\n",
            "I1020 19:22:39.205994 25180 main.go:101] waiting for response for zminion-return-9290dc33-d5a2-5766-f45e-210ca43499ea\n",
            "2017-10-20 19:21:28,127 INFO zen.ZenDisc: Connecting to localhost:8789\n",
            "2017-10-20 19:21:28,416 INFO zen.ZenDisc: Connected to the zenhub/0 instance\n",
            "2017-10-20 19:21:28,985 INFO zen.ZenDisc: Looking for test.example.com\n",
            "2017-10-20 19:21:33,130 INFO zen.ZenDisc: Found IP 1.2.3.4 for device test.example.com\n",
            "2017-10-20 19:21:41,831 INFO zen.ZenDisc: Finished scanning device with address 1.2.3.4\n",
            "2017-10-20 19:21:41,831 INFO zen.ZenDisc: Discovered device test.example.com.\n",
            "2017-10-20 19:21:41,831 INFO zen.ZenDisc: Result: test.example.com\n",
            "2017-10-20 19:21:41,831 INFO zen.ZenDisc: Starting collector loop #001...\n",
            "2017-10-20 19:21:41,831 INFO zen.ZenDisc: Got 1 devices to be scanned during collector loop #001\n",
            "2017-10-20 19:21:42,003 INFO zen.ZenDisc: Filled collection slots for 1 of 1 devices during collector loop #001\n",
            "2017-10-20 19:21:42,003 INFO zen.ZenDisc: skipping WMI-based collection, PySamba zenpack not installed\n",
            "2017-10-20 19:21:42,003 INFO zen.ZenDisc: Collect on device test.example.com for collector loop #001\n",
            "2017-10-20 19:21:42,039 INFO zen.ZenDisc: No Python plugins found for test.example.com\n",
            "2017-10-20 19:21:42,041 INFO zen.ZenDisc: Using SSH collection method for device test.example.com\n",
            "2017-10-20 19:21:42,041 INFO zen.ZenDisc: plugins: zenoss.cmd.uname, zenoss.cmd.linux.df, zenoss.cmd.linux.alt_kernel_name, zenoss.cmd.linux.cpuinfo, zenoss.cmd.linux.interfaces, zenoss.cmd.linux.lvm, zenoss.cmd.linux.memory, zenoss.cmd.linux.netstat_an, zenoss.cmd.linux.netstat_rn, zenoss.cmd.linux.process, zenoss.cmd.linux.rpm, zenoss.cmd.linux.sudo_dmidecode, zenoss.cmd.linux.os_release, zenoss.cmd.linux.os_service\n",
            "2017-10-20 19:21:42,041 INFO zen.ZenDisc: SNMP monitoring off for test.example.com\n",
            "2017-10-20 19:21:42,043 INFO zen.ZenDisc: No portscan plugins found for test.example.com\n",
            "2017-10-20 19:21:52,042 ERROR zen.SshClient: 1.2.3.4 User timeout caused connection failure.\n",
            "2017-10-20 19:21:52,042 INFO zen.CmdClient: command client finished collection for test.example.com\n",
            "2017-10-20 19:21:52,042 INFO zen.ZenDisc: No change in configuration detected\n",
            "2017-10-20 19:21:52,042 INFO zen.ZenDisc: Finished processing client within collector loop #001\n",
            "2017-10-20 19:21:52,043 INFO zen.ZenDisc: Scan time: 10.21 seconds for collector loop #001\n",
            "2017-10-20 19:21:52,043 INFO zen.ZenDisc: Scanned 1 of 1 devices during collector loop #001\n",
            "2017-10-20 19:21:52,043 INFO zen.ZenDisc: Daemon ZenDisc shutting down\n",
            "2017-10-20 19:23:25,655 INFO zen.Job: Job 9ba5c8d7-58de-4f18-96fe-d362841910d3 finished with result 0\n"
        ],
        "logfile": "/opt/zenoss/log/jobs/9ba5c8d7-58de-4f18-96fe-d362841910d3.log",
        "maxLimit": False
    },
    "tid": 1,
    "type": "rpc",
    "method": "detail"
}

nolog = {
    "uuid": "f5259b2f-b4c7-4e97-852e-197b1885e533",
    "action": "JobsRouter",
    "result": {
        "content": [],
        "logfile": "The log file for this job either does not exist or cannot be accessed.",
        "maxLimit": None
    },
    "tid": 1,
    "type": "rpc",
    "method": "detail"
}
