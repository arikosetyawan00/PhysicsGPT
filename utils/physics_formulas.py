"""
Database rumus fisika + mesin penyelesai otomatis.

Setiap rumus disimpan dalam bentuk "equation = 0" (implicit form) memakai
sympy, sehingga solver bisa membalik rumus ke variabel manapun yang belum
diketahui -- tidak perlu menulis versi rumus untuk tiap kemungkinan variabel.
"""

import sympy as sp


# ==========================================
# Database Rumus
# ==========================================
# equation ditulis dalam bentuk "ruas_kiri - ruas_kanan" (artinya = 0).
# Contoh: F = m * a  ->  "F - m*a"

FORMULAS = {

    # ---------------- MECHANICS ----------------
    "Hukum Newton II (F = m·a)": {
        "topic": "Mechanics",
        "equation": "F - m*a",
        "vars": {
            "F": {"label": "Gaya (F)", "unit": "N"},
            "m": {"label": "Massa (m)", "unit": "kg"},
            "a": {"label": "Percepatan (a)", "unit": "m/s²"},
        },
    },
    "Kecepatan (v = v0 + a·t)": {
        "topic": "Mechanics",
        "equation": "v - (v0 + a*t)",
        "vars": {
            "v": {"label": "Kecepatan akhir (v)", "unit": "m/s"},
            "v0": {"label": "Kecepatan awal (v0)", "unit": "m/s"},
            "a": {"label": "Percepatan (a)", "unit": "m/s²"},
            "t": {"label": "Waktu (t)", "unit": "s"},
        },
    },
    "Jarak Tempuh (s = v0·t + ½·a·t²)": {
        "topic": "Mechanics",
        "equation": "s - (v0*t + 0.5*a*t**2)",
        "vars": {
            "s": {"label": "Jarak (s)", "unit": "m"},
            "v0": {"label": "Kecepatan awal (v0)", "unit": "m/s"},
            "a": {"label": "Percepatan (a)", "unit": "m/s²"},
            "t": {"label": "Waktu (t)", "unit": "s"},
        },
    },
    "Kecepatan² (v² = v0² + 2·a·s)": {
        "topic": "Mechanics",
        "equation": "v**2 - (v0**2 + 2*a*s)",
        "vars": {
            "v": {"label": "Kecepatan akhir (v)", "unit": "m/s"},
            "v0": {"label": "Kecepatan awal (v0)", "unit": "m/s"},
            "a": {"label": "Percepatan (a)", "unit": "m/s²"},
            "s": {"label": "Jarak (s)", "unit": "m"},
        },
    },
    "Usaha (W = F·s)": {
        "topic": "Mechanics",
        "equation": "W - F*s",
        "vars": {
            "W": {"label": "Usaha (W)", "unit": "J"},
            "F": {"label": "Gaya (F)", "unit": "N"},
            "s": {"label": "Perpindahan (s)", "unit": "m"},
        },
    },
    "Energi Kinetik (Ek = ½·m·v²)": {
        "topic": "Mechanics",
        "equation": "Ek - 0.5*m*v**2",
        "vars": {
            "Ek": {"label": "Energi Kinetik (Ek)", "unit": "J"},
            "m": {"label": "Massa (m)", "unit": "kg"},
            "v": {"label": "Kecepatan (v)", "unit": "m/s"},
        },
    },
    "Energi Potensial (Ep = m·g·h)": {
        "topic": "Mechanics",
        "equation": "Ep - m*g*h",
        "vars": {
            "Ep": {"label": "Energi Potensial (Ep)", "unit": "J"},
            "m": {"label": "Massa (m)", "unit": "kg"},
            "g": {"label": "Percepatan gravitasi (g)", "unit": "m/s²"},
            "h": {"label": "Ketinggian (h)", "unit": "m"},
        },
    },
    "Momentum (p = m·v)": {
        "topic": "Mechanics",
        "equation": "p - m*v",
        "vars": {
            "p": {"label": "Momentum (p)", "unit": "kg·m/s"},
            "m": {"label": "Massa (m)", "unit": "kg"},
            "v": {"label": "Kecepatan (v)", "unit": "m/s"},
        },
    },
    "Daya (P = W / t)": {
        "topic": "Mechanics",
        "equation": "P - W/t",
        "vars": {
            "P": {"label": "Daya (P)", "unit": "W"},
            "W": {"label": "Usaha (W)", "unit": "J"},
            "t": {"label": "Waktu (t)", "unit": "s"},
        },
    },

    # ---------------- ELECTRICITY ----------------
    "Hukum Ohm (V = I·R)": {
        "topic": "Electricity",
        "equation": "V - I*R",
        "vars": {
            "V": {"label": "Tegangan (V)", "unit": "V"},
            "I": {"label": "Arus (I)", "unit": "A"},
            "R": {"label": "Hambatan (R)", "unit": "Ω"},
        },
    },
    "Daya Listrik (P = V·I)": {
        "topic": "Electricity",
        "equation": "P - V*I",
        "vars": {
            "P": {"label": "Daya (P)", "unit": "W"},
            "V": {"label": "Tegangan (V)", "unit": "V"},
            "I": {"label": "Arus (I)", "unit": "A"},
        },
    },
    "Energi Listrik (W = P·t)": {
        "topic": "Electricity",
        "equation": "W - P*t",
        "vars": {
            "W": {"label": "Energi (W)", "unit": "J"},
            "P": {"label": "Daya (P)", "unit": "W"},
            "t": {"label": "Waktu (t)", "unit": "s"},
        },
    },

    # ---------------- THERMODYNAMICS ----------------
    "Kalor (Q = m·c·ΔT)": {
        "topic": "Thermodynamics",
        "equation": "Q - m*c*dT",
        "vars": {
            "Q": {"label": "Kalor (Q)", "unit": "J"},
            "m": {"label": "Massa (m)", "unit": "kg"},
            "c": {"label": "Kalor jenis (c)", "unit": "J/kg·K"},
            "dT": {"label": "Perubahan suhu (ΔT)", "unit": "K"},
        },
    },

    # ---------------- WAVES & OPTICS ----------------
    "Cepat Rambat Gelombang (v = f·λ)": {
        "topic": "Waves & Optics",
        "equation": "v - f*lam",
        "vars": {
            "v": {"label": "Cepat rambat (v)", "unit": "m/s"},
            "f": {"label": "Frekuensi (f)", "unit": "Hz"},
            "lam": {"label": "Panjang gelombang (λ)", "unit": "m"},
        },
    },
    "Lensa Tipis (1/f = 1/do + 1/di)": {
        "topic": "Waves & Optics",
        "equation": "1/f - (1/do + 1/di)",
        "vars": {
            "f": {"label": "Jarak fokus (f)", "unit": "cm"},
            "do": {"label": "Jarak benda (do)", "unit": "cm"},
            "di": {"label": "Jarak bayangan (di)", "unit": "cm"},
        },
    },

    # ---------------- MODERN PHYSICS ----------------
    "Kesetaraan Massa-Energi (E = m·c²)": {
        "topic": "Modern Physics",
        "equation": "E - m*c**2",
        "vars": {
            "E": {"label": "Energi (E)", "unit": "J"},
            "m": {"label": "Massa (m)", "unit": "kg"},
            "c": {"label": "Kecepatan cahaya (c)", "unit": "m/s"},
        },
    },
}


# ==========================================
# Solver
# ==========================================

class FormulaSolverError(Exception):
    """Dilempar saat rumus tidak bisa diselesaikan dengan input yang diberikan."""


def solve_formula(formula_key: str, known_values: dict):
    """
    Menyelesaikan satu variabel yang belum diketahui dalam sebuah rumus.

    Args:
        formula_key: nama rumus, harus ada di FORMULAS.
        known_values: dict {var_name: nilai_float_atau_None}.
            Variabel dengan nilai None/"" dianggap belum diketahui.

    Returns:
        (unknown_var, hasil_numerik, unit) jika berhasil.

    Raises:
        FormulaSolverError jika jumlah variabel belum diketahui bukan tepat 1,
        atau tidak ditemukan solusi real.
    """

    formula = FORMULAS[formula_key]
    var_names = list(formula["vars"].keys())

    symbols = {name: sp.symbols(name) for name in var_names}
    expr = sp.sympify(formula["equation"], locals=symbols)

    unknowns = [
        name for name in var_names
        if known_values.get(name) in (None, "")
    ]

    if len(unknowns) == 0:
        raise FormulaSolverError(
            "Semua variabel sudah terisi. Kosongkan satu variabel yang "
            "ingin dicari."
        )

    if len(unknowns) > 1:
        raise FormulaSolverError(
            "Isi semua variabel kecuali satu (variabel yang ingin dicari)."
        )

    unknown = unknowns[0]

    substitutions = {}
    for name in var_names:
        if name == unknown:
            continue
        try:
            substitutions[symbols[name]] = float(known_values[name])
        except (TypeError, ValueError):
            raise FormulaSolverError(
                f"Nilai untuk '{formula['vars'][name]['label']}' tidak valid."
            )

    substituted_expr = expr.subs(substitutions)
    solutions = sp.solve(sp.Eq(substituted_expr, 0), symbols[unknown])

    # Ambil solusi real saja (buang solusi kompleks / non-fisis)
    real_solutions = [
        sol for sol in solutions
        if sol.is_real
    ]

    if not real_solutions:
        raise FormulaSolverError(
            "Tidak ditemukan solusi real untuk nilai yang dimasukkan. "
            "Periksa kembali angkanya."
        )

    # Untuk kasus quadratic (misal v² = ...), ambil solusi non-negatif
    # jika ada, karena besaran fisika seperti kecepatan/jarak umumnya positif.
    positive_solutions = [s for s in real_solutions if s >= 0]
    result = positive_solutions[0] if positive_solutions else real_solutions[0]

    unit = formula["vars"][unknown]["unit"]

    return unknown, float(result), unit


def get_topics():
    """Mengembalikan daftar topik unik, terurut."""
    topics = sorted({f["topic"] for f in FORMULAS.values()})
    return topics


def get_formulas_by_topic(topic: str):
    """Mengembalikan daftar nama rumus untuk sebuah topik."""
    return [
        name for name, f in FORMULAS.items()
        if f["topic"] == topic
    ]
