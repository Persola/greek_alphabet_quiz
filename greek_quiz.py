import random

def prompt(alphabet):
    glyph = random.choice(list(glyph_to_grapheme_name.keys()))
    grapheme_name = glyph_to_grapheme_name[glyph]['grapheme_name']
    case = glyph_to_grapheme_name[glyph]['case']
    pronunciation = grapheme_name_to_us_pronunciation[grapheme_name]
    input(f'{glyph}\n')
    print(f'{case} {grapheme_name} ({pronunciation})\n\n')

glyph_to_grapheme_name = {
    'Α': {
        'case': 'uppercase',
        'grapheme_name': 'alpha',
    },
    'α': {
        'case': 'lowercase',
        'grapheme_name': 'alpha',
    },
    'Β': {
        'case': 'uppercase',
        'grapheme_name': 'beta',
    },
    'β': {
        'case': 'lowercase',
        'grapheme_name': 'beta',
    },
    'Γ': {
        'case': 'uppercase',
        'grapheme_name': 'gamma',
    },
    'γ': {
        'case': 'lowercase',
        'grapheme_name': 'gamma',
    },
    'Δ': {
        'case': 'uppercase',
        'grapheme_name': 'delta',
    },
    'δ': {
        'case': 'lowercase',
        'grapheme_name': 'delta',
    },
    'Ε': {
        'case': 'uppercase',
        'grapheme_name': 'epsilon',
    },
    'ε': {
        'case': 'lowercase',
        'grapheme_name': 'epsilon',
    },
    'Ζ': {
        'case': 'uppercase',
        'grapheme_name': 'zeta',
    },
    'ζ': {
        'case': 'lowercase',
        'grapheme_name': 'zeta',
    },
    'Η': {
        'case': 'uppercase',
        'grapheme_name': 'eta',
    },
    'η': {
        'case': 'lowercase',
        'grapheme_name': 'eta',
    },
    'Θ': {
        'case': 'uppercase',
        'grapheme_name': 'theta',
    },
    'θ': {
        'case': 'lowercase',
        'grapheme_name': 'theta',
    },
    'Ι': {
        'case': 'uppercase',
        'grapheme_name': 'iota',
    },
    'ι': {
        'case': 'lowercase',
        'grapheme_name': 'iota',
    },
    'Κ': {
        'case': 'uppercase',
        'grapheme_name': 'kappa',
    },
    'κ': {
        'case': 'lowercase',
        'grapheme_name': 'kappa',
    },
    'Λ': {
        'case': 'uppercase',
        'grapheme_name': 'lambda',
    },
    'λ': {
        'case': 'lowercase',
        'grapheme_name': 'lambda',
    },
    'Μ': {
        'case': 'uppercase',
        'grapheme_name': 'mu',
    },
    'μ': {
        'case': 'lowercase',
        'grapheme_name': 'mu',
    },
    'Ν': {
        'case': 'uppercase',
        'grapheme_name': 'nu',
    },
    'ν': {
        'case': 'lowercase',
        'grapheme_name': 'nu',
    },
    'Ξ': {
        'case': 'uppercase',
        'grapheme_name': 'xi',
    },
    'ξ': {
        'case': 'lowercase',
        'grapheme_name': 'xi',
    },
    'Ο': {
        'case': 'uppercase',
        'grapheme_name': 'omicron',
    },
    'ο': {
        'case': 'lowercase',
        'grapheme_name': 'omicron',
    },
    'Π': {
        'case': 'uppercase',
        'grapheme_name': 'pi',
    },
    'π': {
        'case': 'lowercase',
        'grapheme_name': 'pi',
    },
    'Ρ': {
        'case': 'uppercase',
        'grapheme_name': 'rho',
    },
    'ρ': {
        'case': 'lowercase',
        'grapheme_name': 'rho',
    },
    'Σ': {
        'case': 'uppercase',
        'grapheme_name': 'sigma',
    },
    'σ': {
        'case': 'lowercase',
        'grapheme_name': 'sigma',
    },
    'ς': {
        'case': 'lowercase',
        'grapheme_name': 'sigma',
    },
    'Τ': {
        'case': 'uppercase',
        'grapheme_name': 'tau',
    },
    'τ': {
        'case': 'lowercase',
        'grapheme_name': 'tau',
    },
    'Υ': {
        'case': 'uppercase',
        'grapheme_name': 'upsilon',
    },
    'υ': {
        'case': 'lowercase',
        'grapheme_name': 'upsilon',
    },
    'Φ': {
        'case': 'uppercase',
        'grapheme_name': 'phi',
    },
    'φ': {
        'case': 'lowercase',
        'grapheme_name': 'phi',
    },
    'Χ': {
        'case': 'uppercase',
        'grapheme_name': 'chi',
    },
    'χ': {
        'case': 'lowercase',
        'grapheme_name': 'chi',
    },
    'Ψ': {
        'case': 'uppercase',
        'grapheme_name': 'psi',
    },
    'ψ': {
        'case': 'lowercase',
        'grapheme_name': 'psi',
    },
    'Ω': {
        'case': 'uppercase',
        'grapheme_name': 'omega',
    },
    'ω': {
        'case': 'lowercase',
        'grapheme_name': 'omega'
    },
}

# These pronunciations are for US English. They won't match classical Greek,
# modern Greek, other languages, or other dialects of English, and aren't very
# consistent even within US English.
grapheme_name_to_us_pronunciation = {
    'alpha': 'ˈal-fuh',
    'beta': 'ˈbay-tuh',
    'gamma': 'ˈgam-uh (like "ram")',
    'delta': 'ˈdel-tuh',
    'epsilon': '(ˈep-sil-ˌon) or (ˈep-suh-ˌlon)',
    'zeta': 'ˈzay-tuh',
    'eta': 'ˈay-tuh',
    'theta': 'ˈthay-tuh',
    'iota': 'eye-ˈoh-tuh',
    'kappa': 'ˈkap-uh',
    'lambda': 'ˈlam-duh (like "ram")',
    'mu': 'mew',
    'nu': 'new',
    'xi': '(ksai) or (zai)',
    'omicron': 'ˈoh-mih-ˌkron',
    'pi': 'pai',
    'rho': 'row',
    'sigma': 'ˈsig-muh',
    'tau': 'tao',
    'upsilon': 'ˈup-suh-ˌlon',
    'phi': 'fai',
    'chi': 'kai',
    'psi': '(sai) or (psai)',
    'omega': '(oh-ˈmay-guh) or (oh-ˈmeg-uh)'
}

while(True):
    prompt(glyph_to_grapheme_name)
