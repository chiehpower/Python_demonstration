from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterable

from google.cloud import compute_v1


def list_all_instances(
    project_id: str,
) -> dict[str, Iterable[compute_v1.Instance]]:
    """
    Returns a dictionary of all instances present in a project, grouped by their zone.

    Args:
        project_id: project ID or project number of the Cloud project you want to use.
    Returns:
        A dictionary with zone names as keys (in form of "zones/{zone_name}") and
        iterable collections of Instance objects as values.
    """
    instance_client = compute_v1.InstancesClient()
    request = compute_v1.AggregatedListInstancesRequest()
    request.project = project_id
    # Use the `max_results` parameter to limit the number of results that the API returns per response page.
    request.max_results = 50

    agg_list = instance_client.aggregated_list(request=request)

    all_instances = defaultdict(list)
    # print("Instances found:")
    # Despite using the `max_results` parameter, you don't need to handle the pagination
    # yourself. The returned `AggregatedListPager` object handles pagination
    # automatically, returning separated pages as you iterate over the results.
    for zone, response in agg_list:
        if response.instances:
            all_instances[zone].extend(response.instances)
            # print(f" {zone}:")
            # for instance in response.instances:
                # print(f" - {instance.name} ({instance.machine_type})")
    return all_instances


def format_instance_info(all_instances: dict[str, Iterable[compute_v1.Instance]]) -> str:
    instance_info = []
    for zone, instances in all_instances.items():
        instance_info.append(f"{zone}:")
        for instance in instances:
            instance_info.append(f" - {instance.name} ({instance.status})")

    if not instance_info:
        return '目前沒有運行的 VM。'

    return '\n'.join(instance_info)
