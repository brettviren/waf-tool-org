
def configure(cfg):
    cfg.load("org", tooldir=".")

def build(bld):
    bld.load("org", tooldir=".")

    a = bld.path.find_resource("a.org")
    ahtml = a.parent.make_node("a.html")

    bld(features="org2pdf", source="a.org")
    bld(features="org2pdf", source="a.org",
        target="my-file-different-name.pdf")
    bld(features="org2pdf", source="a.org",
        target=bld.path.find_or_declare("aa.pdf"))
    bld(features="org2pdf", source="a.org",
        target=bld.path.find_or_declare("bb.pdf"))
    # bld(features="org2pdf", source="a.org",
    #     target=bld.path.find_or_declare("bb.pdf"))
    bld(features="org2html", source="a.org",
        target=ahtml)
    # bld.org2html(source="a.org")
    # bld.org2pdf(source="a.org")


