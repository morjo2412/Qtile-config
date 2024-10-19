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
# Make sure 'qtile-extras' is installed or this config will not work.
from qtile_extras import widget
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
    "background": "#191724",  # Fondo oscuro
    "foreground": "#e0def4",  # Texto claro
    "black": "#1a1a1a",       # Negro
    "red": "#eb6f92",         # Rojo
    "green": "#31748f",       # Verde
    "yellow": "#8f7431",      # Amarillo
    "blue": "#9ccfd8",        # Azul
    "orange": "#f6a87a",      # Naranja cálido
    "dark-orange": "#d16a3c",  # Naranja quemado
    "green-moss": "#4f7942",     # Verde musgo oscuro
    "green-forest": "#1f4d3d",
    "green-lime": "#7ebd26",      # Verde lima
    "green-mint": "#74d18f",      #verde menta
    "turquesa": "#2ba7a7",    #turquesa
    "dark-blue": "#314d8f",   # Dark Blue
    "magenta": "#8f3174",     # Magenta
    "magenta2": "#FF00FF",
    "cyan": "#56bcc0",        # Cian
    "gray": "#2e2e2e",        # Gray
    "white": "#e0def4",       # Blanco
    "active": "#C71585",      # Color activo
    "inactive": "#2e2e2e",    # Color inactivo 
    "border_focus": "#9ccfd8",  # Borde enfocado
    "border_normal": "#191724",  # Borde normal
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

    # Lanzar aplicaciones
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

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
    1: Group(">_ Terminal"),
    2: Group("Browser"),
    3: Group("Develop"),
    4: Group("Files"),
    0: Group("Other")
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

layouts = [

     layout.MonadTall(
	border_width= 2, 
	border_focus = Rosa_1 ,
	margin = 4,            
     ),

     layout.Max(border_focus = Rosa_1, border_normal = Rosa_1, border_width = 4, margin = 4),
     
     layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),

    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(border_width= 4,
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]



################################################################################################

# Widgets

# Configuración de los widgets
widget_defaults = dict(
    font="Fira Sans Book",
    fontsize=18,
    padding=5,
    foreground=colors["foreground"],  # Color de texto
    background=colors["background"],  # Fondo
)
extension_defaults = widget_defaults.copy()

# Pantallas y barras
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_color=[colors["magenta"], colors["cyan"]],
                    highlight_method="border",
                    spacing=5,
                    inactive=colors["dark-orange"],
                    active=colors["green"],
                    block_highlight_text_color=colors["foreground"],
                    borderwidth=3,
                    padding=5,
                    this_current_screen_border=colors["magenta"],
                    this_screen_border=colors["inactive"],
                    other_screen_border=colors["border_normal"],
                    other_current_screen_border=colors["inactive"],
                ),
                widget.Prompt(
                    foreground=colors["yellow"],
                    background=colors["background"],
                ),
                widget.WindowName(
                    foreground=colors["cyan"],
                    background=colors["background"],
                    format='{name}',
                    padding=10,
                ),
                widget.Spacer(length=bar.STRETCH),
                widget.CurrentLayout(
                    foreground=colors["foreground"],
                    background=colors["background"],
                    padding=5,
                    decorations=[
                          RectDecoration(
                            colour=colors["green"],
                            radius=10,
                            filled=True,
                            padding_y=5
                        )
                    ],
                ),
                widget.CurrentLayoutIcon(
                    foreground=colors["foreground"],
                    background=colors["background"],
                    scale=0.5,
                    padding=5,
                    decorations=[
                        RectDecoration(
                            colour=colors["green"],
                            radius=10,
                            filled=True,
                            padding_y=5
                        )
                    ],
                ),
                widget.Clock(
                    format='⏱ %d-%m-%Y %a %I:%M %p',
                    foreground=colors["foreground"],
                    background=colors["background"],
                    padding=10,
                    decorations=[
                        RectDecoration(
                            colour=colors["green"],
                            radius=10,
                            filled=True,
                            padding_y=5
                        )
                    ],
                ),
                widget.Battery(
                    foreground=colors["foreground"],
                    background=colors["background"],
                    format='{char} {percent:2.0%}',
                    padding=10,
                    low_foreground=colors["green-moss"],
                    low_percentage=0.2,
                    decorations=[
                        RectDecoration(
                            colour=colors["magenta"],
                            radius=10,
                            filled=True,
                            padding_y=5
                        )
                    ],
                ),
                widget.Volume(
                    foreground=colors["foreground"],
                    background=colors["background"],
                    fmt = '🕫  Vol: {}',
                    padding=10,
                    decorations=[
                        RectDecoration(
                            colour=colors["dark-orange"],
                            radius=8,
                            filled=True,
                            padding_y=5
                        )
                    ],
                ),
                widget.QuickExit(
                    default_text="Salir",
                    foreground=colors["foreground"],
                    background=colors["background"],
                    countdown_format="[ {} ]",
                    padding=10,
                    decorations=[
                        RectDecoration(
                            colour=colors["green"],
                            radius=8,
                            filled=True,
                            padding_y=5
                        )
                    ],
                ),
                widget.Systray(
		    background=colors["background"],
		    padding=0,
		    decorations=[
			RectDecoration(
			    colour=colors["magenta"],
			    radius=8,
			    filled=True,
			    padding_y=5
			)
		    ],
		),
            ],
            40,  # Altura de la barra
            background=colors["background"],  # Fondo de la barra
            opacity=0.9,
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
