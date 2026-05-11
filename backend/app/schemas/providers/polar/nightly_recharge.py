from pydantic import BaseModel


class NightlyRechargeJSON(BaseModel):
    polar_user: str | None = None
    date: str | None = None
    heart_rate_avg: int | None = None
    beat_to_beat_avg: int | None = None
    heart_rate_variability_avg: int | None = None
    breathing_rate_avg: float | None = None
    nightly_recharge_status: int | None = None
    ans_charge: float | None = None
    ans_charge_status: int | None = None
    hrv_samples: dict[str, int] | None = None
    breathing_samples: dict[str, float] | None = None


class NightlyRechargeResponseJSON(BaseModel):
    recharges: list[NightlyRechargeJSON] | None = None
