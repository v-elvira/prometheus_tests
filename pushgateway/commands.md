```
cat <<EOF | curl --data-binary @- -XPOST http://localhost:9091/metrics/job/example-job
# HELP example_metrics_for_pushgateway Example of a metric sent to Pushgateway.
# TYPE example_metrics_for_pushgateway counter
example_metrics_for_pushgateway{label="value"} 117
EOF
```
--data-binay: (not --data, -d) as is, do not modify the data

@: data from stdin

(curl -XPOST http://localhost:9091/metrics/job/example-job --data-binary @- <<EOF) delimiter after <<, then text, possible multiline
____________________________________

```
cat <<EOF | curl --data-binary @- -XPOST http://localhost:9091/metrics/job/gitlab-ci/branch/main/project/prometheus
# HELP ci_pipeline_status Status of the latest CI/CD pipeline
# TYPE ci_pipeline_status gauge
ci_pipeline_status 1
# HELP ci_job_duration_seconds Duration of the CI/CD job in seconds
# TYPE ci_job_duration_seconds gauge
ci_job_duration_seconds 135
EOF
```
label/label_value format

to delete form pushgateway:
```
curl -XDELETE http://localhost:9091/metrics/job/gitlab-ci/branch/main/project/prometheus
```