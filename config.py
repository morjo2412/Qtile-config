# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


#librerias de python


import os
import subprocess
from libqtile import bar, extension, hook, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from libqtile.widget import backlight
# Make sure 'qtile-extras' is installed or this config will not work.
from qtile_extras import widget
from qtile_extras.widget import AnimatedImage
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.widget.decorations import BorderDecoration
from qtile_extras.widget.decorations import PowerLineDecoration

#from qtile_extras.widget import StatusNotifier
#import colors

#############################################################################################

# variables

mod = "mod4"

terminal = "gnome-terminal"

# variables para rofi
 # lanzar rofi
rofi = "rofi -show-icons -show drun"

#Variables de color
Rosa_1 = "eb2387"	

# Paleta de colores Omni
colors = {
    "active": "#C71585",      # Color activo
    "inactive": "#2e2e2e",    # Color inactivo 
    "border_focus": "#9ccfd8",  # Borde enfocado
    "border_normal": "#191724",  # Borde normal

    
    "background": "#0E0B16",      # Fondo oscuro (como el cielo nocturno del juego)
    "foreground": "#E0DFE3",       # Texto claro
    
    "pink": "#FF2C7C",            # Rosa neón (como los elementos de interfaz del juego)
    "off_pink": "#852046",
    
    "cyan": "#00F3FF",            # Cian brillante (para resaltar)
    "blue": "#6FD8E8",        # Azul eléctrico
    "off_cyan": "#5E9CA0",
    "gray_blue": "#4A6D79",
    
    "purple": "#5533c7",          # Morado eléctrico (accesos y detalles)
    "neon_purple": "#C792EA",
    
    "accent_green": "#2CFFAF",    # Verde neón (para métricas)
    "green": "#31748f",       # Verde
    
    "alert": "#FF6B6B",           # Rojo/rosa para alertas (batería baja)
    "red_blood" : "#d94f5f",
    "yellow": "#8f7431",      # Amarillo
    
    "dark_gray": "#1A1823",       # Gris oscuro (para fondos de widgets)
    "black": "#1a1a1a",       # Negro
    
    "warm_orange": "#F6A878",
}


############################################################################################

# Atajos de Teclado

keys = [

    # Navegación entre ventanas
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),

    # Mover ventanas usando las teclas de dirección
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Cambiar el tamaño de las ventanas
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),

    # Atajos específicos para el layout 'MonadTall'
    Key([mod], "period", lazy.layout.grow(), desc="Grow window in MonadTall layout"),
    Key([mod], "comma", lazy.layout.shrink(), desc="Shrink window in MonadTall layout"),
    Key([mod], "o", lazy.layout.maximize(), desc="Maximize the window"),
    Key([mod, "shift"], "space", lazy.layout.flip(), desc="Flip layout"),

    # Alternar entre stack dividido y no dividido
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

    # Teclas multimedia
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +3%"), desc="Raise brightness level by 3%"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 3-%"), desc="Lower brightness level by 3%"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset Master 3%+"), desc="Raise volume level by 3%"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset Master 3%-"), desc="Lower volume level by 3%"),
    Key([], "XF86AudioMute", lazy.spawn("amixer sset Master 1+ toggle"), desc="Mute or unmute volume level"),

    # Comandos del sistema
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "mod1"], "s", lazy.spawn("systemctl poweroff"), desc="Shutdown System"),
    Key([mod, "mod1"], "r", lazy.spawn("systemctl reboot"), desc="Reboot System"),


    # Lanzar aplicaciones
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "n", lazy.spawn("firefox"), desc="Open firefox"),

    # Lanzar rofi
    Key(["mod1"], "d", lazy.spawn(rofi), desc="Lanzar Rofi"),
    
    # Tomar captura de pantalla usando Flameshot
    Key([], "Print", lazy.spawn("flameshot gui"), desc = "Imprimir Pantalla")
]


#final de los atajos de teclado

#####################################################################################################






# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


# usaremos gurpos para uso especifico

#groups = [Group(i) for i in "1234567890"]

__groups = {
    1: Group("1"),
    2: Group("2"),
    3: Group("3"),
    4: Group("4"),
    5: Group("5"),
    6: Group("6")
}
groups = [__groups[i] for i in __groups]


def get_group_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]


for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], str(get_group_key(i.name)), lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1+shift+letter of group = switch to & move focused window to group
        Key([mod, "shift"], str(get_group_key(i.name)),
            lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])
    
layout_theme = {
    "border_width": 2,                   # Grosor del borde
    "border_focus": colors["pink"],    # Borde de la ventana enfocada
    "border_normal": colors["cyan"],     # Borde de ventanas inactivas
    "margin": 3,                         # Espacio exterior alrededor de las ventanas
    "single_border_width": 3,           # Grosor del borde si hay una sola ventana
    "single_margin": 5,                 # Margen si hay una sola ventana
    "ratio": 0.4,                        # Proporción inicial del área principal
}

layouts = [

    layout.MonadTall(
        **layout_theme,
        # Opciones adicionales para mejor usabilidad:
        change_ratio=0.05,    # Incremento al redimensionar (más preciso)
        min_ratio=0.3,        # Tamaño mínimo del área principal
        max_ratio=0.7,        # Tamaño máximo del área principal
    ),
    
    layout.Spiral(
        **layout_theme,
        direction="right",    # Dirección de la espiral (right/left/up/down)
        split_ratio=0.5,      # Cómo se divide el espacio al añadir ventanas
        # Mejoras de usabilidad:
        new_client_position="bottom",  # Nueva ventana arriba/abajo (top/bottom)
        change_ratio=0.025,   # Incremento más preciso al redimensionar
        max_ratio=0.75,       # Límite máximo de expansión
        min_ratio=0.25,       # Límite mínimo de contracción
    ),

     layout.Max(border_focus = colors["pink"], border_normal = colors["pink"], border_width = 3, margin = 2),
     
    layout.Columns(
        **layout_theme,
        num_columns=2,              # Número inicial de columnas
        split=True,                  # Permite dividir ventanas en subcolumnas
        wrap_focus_columns=True,     # Navegación circular entre columnas
        wrap_focus_rows=True,        # Navegación circular entre filas
        insert_position=1,           # Nueva ventanas a la derecha (0=izquierda)
        fair=False,                  # Las nuevas ventanas ocupan espacio equitativo
        # Mejoras de usabilidad:
        change_ratio=0.025,          # Precisión al redimensionar
        grow_amount=10,              # Píxeles a crecer/encoger con atajos
    ),
]



################################################################################################

# Widgets

# Configuración de los widgets
widget_defaults = dict(
    font="Fira Sans Book",
    fontsize=18
,
    padding=5,
    foreground=colors["foreground"],  # Color de texto
    background=colors["background"],  # Fondo
)
extension_defaults = widget_defaults.copy()

# Pantallas y Barras
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    font="Fira Code Bold",
                    fontsize=16,
                    margin_y=4,
                    margin_x=8,
                    padding_y=6,
                    padding_x=8,
                    active=colors["pink"],
                    inactive=colors["off_pink"],
                    rounded=False,
                    highlight_color=[colors["cyan"], colors["purple"]],
                    highlight_method="block",
                    this_current_screen_border=colors["pink"],
                    block_highlight_text_color=colors["background"],
                    decorations=[
                        RectDecoration(
                            colour=colors["dark_gray"],
                            radius=6,
                            filled=True,
                            padding_y=2,
                        )
                    ],
                ),

		        # Prompt 
                widget.Prompt(
                    foreground=colors["yellow"],
                    background=colors["background"],
                ),
                 
                # Decoracion
                widget.Spacer(
                    length=1,
                    background=colors["dark_gray"],
                    decorations=[
                        PowerLineDecoration(
                            path="forward_slash",
                            size=45,
                            override_colour=colors["dark_gray"],
                        ),
                    ],
                ),
                # Nombre de la ventana actual (estilo minimalista)
                widget.WindowName(
                    background=colors["purple"],
                    foreground=colors["cyan"],
                    font="Iosevka",
                    padding=10,
                    max_chars=0,
                    scroll = True,
                    width = 350,
                    empty_group_string = " Void.................. ",
                    decorations=[
                        PowerLineDecoration(
                            path="forward_slash",
                            size=45,
                            override_colour=colors["purple"]
                
                        ),
                        
                    ],
                ),
                
                # Decoraciones
                widget.Spacer(
                    length=25,
                    background=colors["accent_green"],  # Fondo del Spacer
                    decorations=[
                        PowerLineDecoration(
                            path="forward_slash",
                            size=45,
                            override_colour=colors["accent_green"],  # Color de la flecha
                        ),
                    ],
                ),
                widget.Spacer(
                    length=25,
                    background=colors["pink"],
                    decorations=[
                        PowerLineDecoration(
                            path="forward_slash",
                            size=45,
                            override_colour=colors["pink"],
                        ),
                    ],
                ),
                widget.Spacer(
                    length=25,
                    background=colors["cyan"],
                    decorations=[
                        PowerLineDecoration(
                            path="forward_slash",
                            size=45,
                            override_colour=colors["cyan"],
                        ),
                    ],
                ),
                
                widget.Spacer(length= bar.STRETCH),
                
                # Current Layout
                widget.CurrentLayoutIcon(
                    foreground=colors["cyan"],
                    background=colors["background"],
                    scale=0.5,
                    padding=5,
                ),
                
                # Widgets del sistema (estilo "circuitos" neón)
                widget.CPU(
                    foreground=colors["accent_green"],
                    format="  {load_percent}%",
                    padding=8,
                    decorations=[
                        BorderDecoration(
                            border_width=[0, 0, 4, 0],  # Solo abajo
                            colour = colors["accent_green"],
                            padding_y = 2,
                            padding_x = 4,
                        ),
                    ],
                ),
                widget.Memory(
                    foreground=colors["pink"],
                    format="  {MemUsed: .0f}{mm}",
                    padding=8,
                    decorations=[
                        BorderDecoration(
                            border_width=[0, 0, 4, 0],  # Solo abajo
                            colour = colors["pink"],
                            padding_y = 2,
                            padding_x = 4,
                        ),
                    ],

                ),

                # Reloj (estilo "digital retro")
                widget.Clock(
                    foreground=colors["cyan"],
                    format="  %d/%m  󰥔  %I:%M %p",
                    padding=10,
                    decorations=[
                        BorderDecoration(
                            border_width=[0, 0, 4, 0],  # Solo abajo
                            colour = colors["cyan"],
                            padding_y = 2,
                            padding_x = 4,
                        ),
                    ],
                ),

                # Batería (estilo de barra de energía del juego)
                widget.Battery(
                    foreground=colors["accent_green"],
                    format="{char} {percent:2.0%}",
                    low_foreground=colors["alert"],
                    low_percentage=0.15,
                    padding=8,
                    decorations=[
                        BorderDecoration(
                            border_width=[0, 0, 4, 0],  # Solo abajo
                            colour = colors["accent_green"],
                            padding_y = 2,
                            padding_x = 4,
                        ),
                    ],
                ),

                # Volumen (icono de altavoz estilo pixel-art)
                widget.Volume(
                    foreground=colors["pink"],
                    fmt="󰕾 {}",
                    padding=8,
                    decorations=[
                        BorderDecoration(
                            border_width=[0, 0, 4, 0],  # Solo abajo
                            colour = colors["pink"],
                            padding_y = 2,
                            padding_x = 4,
                        ),
                    ],
                ),

                # Systray (integrado discretamente)
                widget.Systray(
                    background=colors["dark_gray"],
                    padding=8,
                    icon_size=20,
                    decorations=[
                        BorderDecoration(
                            border_width=[0, 0, 4, 0],  # Solo abajo
                            colour = colors["cyan"],
                            padding_y = 2,
                            padding_x = 4,
                        ),
                    ],
                ),

                # Cerrar Sesion
                widget.QuickExit(
                    default_text="󰍃 ",
                    foreground=colors["neon_purple"],
                    background=colors["background"],
                    countdown_format="[{}]",
                    countdown_start=3,
                    padding=10,
                    decorations=[
                        BorderDecoration(
                            border_width=[0, 0, 4, 0],  # Solo abajo
                            colour = colors["purple"],
                            padding_y = 2,
                            padding_x = 4,
                        ),
                    ],
                ),
                
                # Fondo de Pantalla
                widget.Wallpaper(
                directory = "~/Pictures/Wallpapers/Neon",
                random_selection = "TRUE",
                wallpaper_command = ['feh', '--bg-fill'],
                foreground=colors["green"],
                label="󰉏",
                timeout=5,
                ),
            ],
            40,  # Altura de la barra
            background = colors["background"],  # Fondo de la barra
            opacity=1,
        ),
    ),
    
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    font="Fira Code Bold",
                    fontsize=16,
                    margin_y=4,
                    margin_x=8,
                    padding_y=6,
                    padding_x=8,
                    active=colors["pink"],
                    inactive=colors["off_pink"],
                    rounded=False,
                    highlight_color=[colors["cyan"], colors["purple"]],
                    highlight_method="block",
                    this_current_screen_border=colors["pink"],
                    block_highlight_text_color=colors["background"],
                    decorations=[
                        RectDecoration(
                            colour=colors["dark_gray"],
                            radius=6,
                            filled=True,
                            padding_y=2,
                        )
                    ],
                ),
                widget.Prompt(),
                widget.WindowName(),
                # Reloj (estilo "digital retro")
                widget.Clock(
                    foreground=colors["cyan"],
                    format="  %d/%m  󰥔  %I:%M %p",
                    padding=10,
                    decorations=[
                        BorderDecoration(
                            border_width=[0, 0, 4, 0],  # Solo abajo
                            colour = colors["cyan"],
                            padding_y = 2,
                            padding_x = 4,
                        ),
                    ],
                ),
            ],
            40,
        ),
    ),
]


###########################################################################################

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

11

