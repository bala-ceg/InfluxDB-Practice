curl --request POST \
  https://ap-southeast-2-1.aws.cloud2.influxdata.com/api/v2/query  \
  --header 'Authorization: 2KdXsJPE0yGpwxm6ybELC9-VjHYLN32QDTcNpRZUOVlgFJqJC7aUSLKcl26YwFP9_9jHqoih7FUWIy_zaIxfuw==' \
  --header 'Accept: application/csv' \
  --header 'Content-type: application/vnd.flux' \
  --data 'from(bucket:"airbyte")
        |> range(start: -1h)
        |> filter(fn: (r) => r._measurement == "wifi_status")
        |> aggregateWindow(every: 10m, fn: mean)'


curl --request GET https://ap-southeast-2-1.aws.cloud2.influxdata.com/api/v2/orgs \     
  --header "Authorization: Token 2KdXsJPE0yGpwxm6ybELC9-VjHYLN32QDTcNpRZUOVlgFJqJC7aUSLKcl26YwFP9_9jHqoih7FUWIy_zaIxfuw==" \
  --header "Accept: application/json" \
  --header "Content-Type: application/json"


curl https://ap-southeast-2-1.aws.cloud2.influxdata.com/api/v2/orgs=org-1 --header "Authorization: Token 2KdXsJPE0yGpwxm6ybELC9-VjHYLN32QDTcNpRZUOVlgFJqJC7aUSLKcl26YwFP9_9jHqoih7FUWIy_zaIxfuw=="




curl --request POST 'https://ap-southeast-2-1.aws.cloud2.influxdata.com/api/v2/query' \
--header 'Content-Type: application/vnd.flux' \
--header 'Accept: application/csv \
--header 'Authorization: Token 2KdXsJPE0yGpwxm6ybELC9-VjHYLN32QDTcNpRZUOVlgFJqJC7aUSLKcl26YwFP9_9jHqoih7FUWIy_zaIxfuw==' \
--data 'from(bucket: "airbyte")
          |> range(start: -5m)
          |> filter(fn: (r) => r._measurement == "wifi_status")'



curl --get "https://ap-southeast-2-1.aws.cloud2.influxdata.com/api/v2" \
  --header "Authorization: 2KdXsJPE0yGpwxm6ybELC9-VjHYLN32QDTcNpRZUOVlgFJqJC7aUSLKcl26YwFP9_9jHqoih7FUWIy_zaIxfuw==" \
  --header 'Content-type: application/json' \
  --data-urlencode "db=mydb" \
  --data-urlencode "q=SELECT * FROM cpu_usage"
