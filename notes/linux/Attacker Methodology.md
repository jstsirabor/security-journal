|Step|Command|Question it answers|
|---|---|---|
|1|`id && sudo -l`|Who am I and what can I already do?|
|2|`ps aux \| grep root`|What root processes are potential targets?|
|3|`ss -tulnp`|What services are listening — internal and external?|
|4|`lsof -i :portNumber`|What's actively happening on that specific port?|
|5|`ps aux \| grep processName`|What are the full details of that process — arguments, user, credentials?|
