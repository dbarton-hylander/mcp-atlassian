from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mcp_atlassian.confluence.config import ConfluenceConfig
    from mcp_atlassian.jira.config import JiraConfig


@dataclass(frozen=True)
class MainAppContext:
    """
    Context holding Atlassian service configurations loaded at server startup.

    ``full_*`` configs represent globally authenticated service configs that can
    be used without request-scoped credentials.

    ``base_*`` configs preserve non-secret service settings such as URLs,
    proxies, filters, and SSL options so HTTP requests with per-user
    Authorization headers can still build request-scoped clients.
    """

    full_jira_config: JiraConfig | None = None
    full_confluence_config: ConfluenceConfig | None = None
    base_jira_config: JiraConfig | None = None
    base_confluence_config: ConfluenceConfig | None = None
    read_only: bool = False
    enabled_tools: list[str] | None = None
    enabled_toolsets: set[str] | None = None
