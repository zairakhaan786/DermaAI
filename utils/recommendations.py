"""
DermaAI – Recommendation Engine
================================
Provides severity classification and skincare recommendations
for each of the 9 skin conditions detected by DermaAI.

Usage:
    from utils.recommendations import get_recommendation
    data = get_recommendation("Melanoma")
    # -> { "severity": "Severe", "treatment": ..., "prevention": ..., "routine": ..., "severity_class": "severe" }
"""

# ────────────────────────────────────────────────────────────────────────────
# Recommendation Database
# Each key maps to a dict with severity and skincare guidance.
# severity_class drives the CSS colour chip: "mild" | "moderate" | "severe"
# ────────────────────────────────────────────────────────────────────────────

RECOMMENDATIONS: dict[str, dict] = {
    "Actinic Keratosis": {
        "severity": "Moderate",
        "severity_class": "moderate",
        "treatment": (
            "Consult a dermatologist for cryotherapy, topical fluorouracil, or "
            "imiquimod cream. Avoid self-treatment — professional evaluation is essential."
        ),
        "prevention": (
            "Apply broad-spectrum SPF 30+ sunscreen daily. Wear protective clothing and "
            "wide-brimmed hats when outdoors. Avoid tanning beds."
        ),
        "routine": (
            "Morning: gentle cleanser → SPF 50 sunscreen. "
            "Evening: mild exfoliant (AHA) → rich moisturiser. "
            "Visit a dermatologist every 6 months for checks."
        ),
    },
    "Atopic Dermatitis": {
        "severity": "Mild",
        "severity_class": "mild",
        "treatment": (
            "Use prescribed topical corticosteroids or calcineurin inhibitors for flares. "
            "Keep skin well-moisturised. Antihistamines may relieve itch at night."
        ),
        "prevention": (
            "Avoid known triggers (dust mites, pet dander, harsh soaps, fragrances). "
            "Keep indoor humidity around 45–55%. Wear soft, breathable cotton fabrics."
        ),
        "routine": (
            "Morning: lukewarm shower (max 10 min) → fragrance-free moisturiser within 3 min. "
            "Evening: thick emollient cream or ointment (e.g. Cerave, Eucerin). "
            "Avoid hot water, strong detergents, and scratching."
        ),
    },
    "Benign Keratosis": {
        "severity": "Mild",
        "severity_class": "mild",
        "treatment": (
            "Generally no treatment is needed. If it causes discomfort or cosmetic concern, "
            "a dermatologist can remove it via cryotherapy or laser."
        ),
        "prevention": (
            "Protect skin from excessive sun exposure. "
            "Regular dermatology check-ups to monitor any changes in size, colour, or shape."
        ),
        "routine": (
            "Morning: gentle cleanser → antioxidant vitamin C serum → SPF 30+. "
            "Evening: hydrating moisturiser. Monitor the lesion monthly for changes."
        ),
    },
    "Dermatofibroma": {
        "severity": "Mild",
        "severity_class": "mild",
        "treatment": (
            "Usually harmless; no treatment required. "
            "Surgical excision or cryotherapy available if painful or bothersome cosmetically."
        ),
        "prevention": (
            "Avoid scratching or picking at bump. "
            "Protect from minor skin injuries that can trigger formation."
        ),
        "routine": (
            "Morning: gentle cleanser → lightweight moisturiser → SPF 30+. "
            "Evening: nourishing moisturiser. Keep the area clean and avoid irritation."
        ),
    },
    "Melanocytic Nevus": {
        "severity": "Mild",
        "severity_class": "mild",
        "treatment": (
            "Most moles are benign — no treatment needed. "
            "If a mole shows the ABCDE signs (Asymmetry, Border, Colour, Diameter, Evolving) "
            "consult a dermatologist immediately for a biopsy."
        ),
        "prevention": (
            "Daily sun protection (SPF 50+). Avoid UV tanning. "
            "Perform monthly self-examinations and annual full-body dermatology checks."
        ),
        "routine": (
            "Morning: antioxidant serum → SPF 50+ sunscreen. "
            "Evening: retinol or niacinamide serum → moisturiser. "
            "Photograph moles periodically to track changes."
        ),
    },
    "Melanoma": {
        "severity": "Severe",
        "severity_class": "severe",
        "treatment": (
            "URGENT: Seek medical attention immediately. "
            "Treatment options include surgical excision, immunotherapy, targeted therapy, "
            "or radiation — determined by stage. Early-stage detection greatly improves prognosis."
        ),
        "prevention": (
            "Use SPF 50+ broad-spectrum sunscreen every day. Avoid midday sun (10am–4pm). "
            "Never use tanning beds. Wear UV-protective clothing and sunglasses."
        ),
        "routine": (
            "Medical care takes priority. While under treatment: use gentle fragrance-free "
            "cleanser → hyaluronic acid moisturiser → SPF 50+. "
            "Avoid active ingredients (retinol, AHAs) unless cleared by your oncologist."
        ),
    },
    "Squamous Cell Carcinoma": {
        "severity": "Severe",
        "severity_class": "severe",
        "treatment": (
            "Immediate medical evaluation required. "
            "Standard treatment is surgical excision (Mohs surgery for face). "
            "Radiation or systemic therapy may be needed for advanced cases."
        ),
        "prevention": (
            "Rigorous sun protection: SPF 50+, UV-blocking clothing, and wide-brimmed hats. "
            "Stop smoking, as it increases risk. Annual skin cancer screenings recommended."
        ),
        "routine": (
            "During/after treatment: gentle gel cleanser → soothing centella asiatica serum → "
            "non-comedogenic moisturiser → SPF 50+. Avoid all exfoliants and retinol. "
            "Follow dermatologist's wound-care instructions strictly."
        ),
    },
    "Tinea Ringworm Candidiasis": {
        "severity": "Moderate",
        "severity_class": "moderate",
        "treatment": (
            "Use over-the-counter antifungal creams (clotrimazole, miconazole) for 2–4 weeks. "
            "Severe cases require prescription oral antifungals (fluconazole, itraconazole). "
            "Keep the area dry and clean."
        ),
        "prevention": (
            "Keep skin dry, especially skin folds. Wear breathable, moisture-wicking fabrics. "
            "Avoid sharing towels, combs, or footwear. Change socks daily."
        ),
        "routine": (
            "Morning: antifungal body wash → dry skin thoroughly → antifungal powder or cream. "
            "Evening: clean and dry the affected area → apply antifungal cream. "
            "Wash bedding and clothes at high temperature during treatment."
        ),
    },
    "Vascular Lesion": {
        "severity": "Moderate",
        "severity_class": "moderate",
        "treatment": (
            "Options include laser therapy (pulsed-dye laser), intense pulsed light (IPL), "
            "or sclerotherapy depending on lesion type. Consult a vascular specialist or "
            "dermatologist for the most appropriate approach."
        ),
        "prevention": (
            "Protect from sun exposure which can worsen redness. "
            "Avoid extreme temperature changes, spicy foods, and alcohol if rosacea-related."
        ),
        "routine": (
            "Morning: fragrance-free gentle cleanser → green-based colour-correcting SPF 30+. "
            "Evening: soothing centella asiatica or niacinamide serum → "
            "rich non-irritating moisturiser. Avoid hot showers, scrubs, and rubbing."
        ),
    },
}

# Default fallback – displayed if disease name is not found in the database
_DEFAULT_REC: dict = {
    "severity": "Unknown",
    "severity_class": "mild",
    "treatment": "Please consult a certified dermatologist for a thorough, personalised diagnosis.",
    "prevention": "Maintain a consistent skincare routine and protect your skin from excessive sun exposure.",
    "routine": "Use a gentle cleanser, a broad-spectrum SPF 30+ sunscreen, and a hydrating moisturiser daily.",
}


def get_recommendation(disease_name: str) -> dict:
    """
    Return severity and skincare recommendation data for a given disease name.

    Args:
        disease_name: Disease label returned by the AI model.

    Returns:
        A dict with keys: severity, severity_class, treatment, prevention, routine.
    """
    return RECOMMENDATIONS.get(disease_name, _DEFAULT_REC)
