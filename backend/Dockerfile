# =========================
# BUILD STAGE
# =========================
FROM python:3.13-slim AS builder

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /root_project

# uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# deps first (cache layer)
COPY uv.lock pyproject.toml ./

ENV VIRTUAL_ENV=/opt/venv
ENV UV_PROJECT_ENVIRONMENT=/opt/venv

RUN uv venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN uv sync --locked --no-dev --no-install-project

# copy full source
COPY . .

RUN uv sync --locked --no-dev --no-editable


# =========================
# RUNTIME STAGE
# =========================
FROM python:3.13-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libpq5 \
    bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /root_project

# uv (optional but safe for tooling)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# copy venv + app
COPY --from=builder /opt/venv /opt/venv
COPY --from=builder /root_project /root_project

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"
ENV UV_PROJECT_ENVIRONMENT=/opt/venv
ENV UV_NO_SYNC=true

# =========================
# FIX FOR YOUR MAIN ISSUE
# =========================

# ensure script is executable
RUN chmod +x /root_project/scripts/start/app.sh

# safety: ensure bash exists (already installed above)
SHELL ["/bin/bash", "-c"]

# default working directory
WORKDIR /root_project

# expose API
EXPOSE 8000

# =========================
# IMPORTANT: ENTRYPOINT FIX
# =========================

ENTRYPOINT ["bash", "/root_project/scripts/start/app.sh"]