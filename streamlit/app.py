import json
from pathlib import Path
from datetime import datetime
from io import BytesIO
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

import streamlit as st
import streamlit.components.v2 as components
from web3 import Web3

# =========================================================
# 1. KONFIGURASI
# =========================================================

RPC_URL = "http://127.0.0.1:8545"

PROJECT_DIR = Path(__file__).parent

DEPLOYMENT_PATH = PROJECT_DIR / "deployment.json"

ARTIFACT_PATH = (
    PROJECT_DIR
    / "artifacts"
    / "contracts"
    / "SistemVerifikasiIjazah.sol"
    / "SistemVerifikasiIjazah.json"
)

st.set_page_config(
    page_title="Verifikasi Ijazah Akademik",
    page_icon="🎓",
    layout="wide",
)

st.title("🎓 Sistem Verifikasi Ijazah Akademik")
st.caption("Blockchain Hardhat | MetaMask | Streamlit")


# =========================================================
# 2. KOMPONEN METAMASK
# =========================================================

WALLET_HTML = """
<div>
    <button id="connect-wallet" type="button">
        Hubungkan MetaMask
    </button>
    <p id="wallet-status">Wallet belum terhubung.</p>
</div>
"""

WALLET_CSS = """
button {
    padding: 0.7rem 1rem;
    border: none;
    border-radius: 8px;
    background: var(--st-primary-color);
    color: white;
    font-weight: 600;
    cursor: pointer;
}

p {
    color: var(--st-text-color);
    overflow-wrap: anywhere;
}
"""

WALLET_JS = """
export default function(component) {
    const { parentElement, setStateValue } = component;
    const button = parentElement.querySelector("#connect-wallet");
    const status = parentElement.querySelector("#wallet-status");

    let mounted = true;

    async function readWallet() {
        if (!window.ethereum) return;

        const accounts = await window.ethereum.request({
            method: "eth_accounts"
        });

        const chainId = await window.ethereum.request({
            method: "eth_chainId"
        });

        if (!mounted) return;

        const connected = Boolean(accounts && accounts.length > 0);
        const address = connected ? accounts[0] : "";

        setStateValue("wallet", {
            address,
            chainId,
            connected
        });

        status.textContent = connected
            ? "Wallet terhubung: " + address
            : "Wallet belum terhubung.";
    }

    async function connectWallet() {
        if (!window.ethereum) {
            status.textContent = "MetaMask tidak ditemukan.";
            return;
        }

        try {
            status.textContent = "Menunggu persetujuan...";

            await window.ethereum.request({
                method: "eth_requestAccounts"
            });

            await readWallet();

        } catch (error) {
            status.textContent = "Koneksi gagal: " + error.message;
        }
    }

    function onAccountsChanged() {
        readWallet().catch(() => {});
    }

    function onChainChanged() {
        readWallet().catch(() => {});
    }

    button.addEventListener("click", connectWallet);

    if (window.ethereum) {
        window.ethereum.on("accountsChanged", onAccountsChanged);
        window.ethereum.on("chainChanged", onChainChanged);

        readWallet().catch(() => {});
    }

    return () => {
        mounted = false;

        button.removeEventListener("click", connectWallet);

        if (window.ethereum && window.ethereum.removeListener) {
            window.ethereum.removeListener(
                "accountsChanged", onAccountsChanged
            );

            window.ethereum.removeListener(
                "chainChanged", onChainChanged
            );
        }
    };
}
"""

wallet_component = components.component(
    name="ijazah_metamask_wallet",
    html=WALLET_HTML,
    css=WALLET_CSS,
    js=WALLET_JS,
)


# =========================================================
# 3. KONEKSI WEB3.PY
# =========================================================

w3 = Web3(
    Web3.HTTPProvider(
        RPC_URL,
        request_kwargs={"timeout": 5}
    )
)


# =========================================================
# 4. CEK KONEKSI BLOCKCHAIN
# =========================================================

if not w3.is_connected():
    st.error(
        "Tidak dapat terhubung ke Hardhat Network. "
        "Pastikan Hardhat Node sedang berjalan."
    )
    st.stop()


# =========================================================
# 5. LOAD CONTRACT ADDRESS
# =========================================================

if not DEPLOYMENT_PATH.exists():
    st.error(
        "File deployment.json tidak ditemukan. "
        "Silakan deploy smart contract terlebih dahulu."
    )
    st.stop()

with open(DEPLOYMENT_PATH, "r", encoding="utf-8") as file:
    deployment_data = json.load(file)

CONTRACT_ADDRESS = Web3.to_checksum_address(
    deployment_data["address"]
)


# =========================================================
# 6. LOAD CONTRACT ABI
# =========================================================

if not ARTIFACT_PATH.exists():
    st.error(
        "Artifact smart contract tidak ditemukan. "
        "Silakan compile smart contract terlebih dahulu."
    )
    st.stop()

with open(ARTIFACT_PATH, "r", encoding="utf-8") as file:
    contract_artifact = json.load(file)

CONTRACT_ABI = contract_artifact["abi"]


# =========================================================
# 7. INISIALISASI SMART CONTRACT
# =========================================================

contract = w3.eth.contract(
    address=CONTRACT_ADDRESS,
    abi=CONTRACT_ABI
)


# =========================================================
# 8. STATUS BLOCKCHAIN
# =========================================================

st.subheader("1. Status Blockchain Lokal")

col1, col2, col3 = st.columns(3)

col1.metric("Chain ID", w3.eth.chain_id)
col2.metric("Block Terbaru", w3.eth.block_number)
col3.metric("Status", "Terhubung")

st.caption("Contract Address:")
st.code(CONTRACT_ADDRESS)

st.divider()


# =========================================================
# 9. KONEKSI METAMASK
# =========================================================

st.subheader("2. Hubungkan MetaMask")

wallet_result = wallet_component(
    key="ijazah_metamask",
    default={
        "wallet": {
            "address": "",
            "chainId": "",
            "connected": False
        }
    },
    on_wallet_change=lambda: None,
)

wallet = wallet_result.wallet

wallet_connected = (
    wallet
    and wallet.get("connected")
    and wallet.get("address")
)

is_admin = False

if wallet_connected:

    wallet_address = Web3.to_checksum_address(
        wallet["address"]
    )

    st.success("Wallet berhasil terhubung.")
    st.code(wallet_address)

    try:
        wallet_chain_id = int(wallet["chainId"], 16)

        if wallet_chain_id != w3.eth.chain_id:
            st.error("Pilih jaringan Hardhat Local di MetaMask.")
            st.stop()

        if wallet_address != Web3.to_checksum_address(
            w3.eth.accounts[0]
        ):
            st.warning(
                "Wallet bukan admin. "
                "Gunakan akun Hardhat #0 untuk fitur admin."
            )
            is_admin = False

        else:
            st.success("Wallet terhubung sebagai ADMIN.")
            is_admin = True

    except (ValueError, TypeError):
        st.error("Chain ID MetaMask tidak valid.")
        st.stop()

else:
    st.info("Hubungkan MetaMask terlebih dahulu.")

st.divider()


# =========================================================
# 10. INFORMASI ADMIN DAN SALDO
# =========================================================

st.subheader("3. Informasi Admin")

admin_address = Web3.to_checksum_address(
    w3.eth.accounts[0]
)

st.write("Alamat admin:")
st.code(admin_address)

balance = w3.eth.get_balance(admin_address)

balance_eth = w3.from_wei(
    balance,
    "ether"
)

st.metric(
    "Saldo Admin",
    f"{float(balance_eth):.6f} ETH"
)


# =========================================================
# 11. FITUR APLIKASI
# =========================================================

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "Tambah Ijazah",
    "Verifikasi",
    "Data Ijazah",
    "Cabut Ijazah",
    "Informasi NFT",
    "Cetak Ijazah",
    "Riwayat Verifikasi"
])


# =========================================================
# TAB 1: TAMBAH IJAZAH
# =========================================================

with tab1:

    st.subheader("Tambah Ijazah Baru")

    st.caption(
        "Fitur ini hanya dapat digunakan oleh admin."
    )

    with st.form("form_tambah_ijazah"):

        nama = st.text_input("Nama Lengkap")

        nim = st.text_input("NIM")

        prodi = st.text_input("Program Studi")

        nomor = st.text_input("Nomor Ijazah")

        tahun = st.number_input(
            "Tahun Lulus",
            min_value=1,
            max_value=2100,
            value=2026
        )

        pemilik = st.text_input(
            "Alamat Wallet Pemilik NFT"
        )

        submit_tambah = st.form_submit_button(
            "Tambah Ijazah",
            type="primary"
        )

    if submit_tambah:

        if not is_admin:

            st.error(
                "Hanya admin yang dapat menambahkan ijazah."
            )

        elif not all([
            nama.strip(),
            nim.strip(),
            prodi.strip(),
            nomor.strip(),
            pemilik.strip()
        ]):

            st.error("Semua data wajib diisi.")

        elif not Web3.is_address(pemilik):

            st.error("Alamat wallet pemilik tidak valid.")

        else:

            try:

                pemilik = Web3.to_checksum_address(
                    pemilik
                )

                tx_hash = contract.functions.tambahIjazah(
                    nama,
                    nim,
                    prodi,
                    nomor,
                    int(tahun),
                    pemilik
                ).transact({
                    "from": admin_address
                })

                receipt = w3.eth.wait_for_transaction_receipt(
                    tx_hash
                )

                if receipt.status == 1:

                    token_id = contract.functions.getTokenId(
                        nomor
                    ).call()

                    st.success(
                        "Ijazah berhasil ditambahkan!"
                    )

                    st.write("Token ID:", token_id)

                    st.code(tx_hash.hex())

                else:

                    st.error("Transaksi gagal.")

            except Exception as error:

                st.error("Gagal menambahkan ijazah.")

                st.caption(str(error))


# =========================================================
# TAB 2: VERIFIKASI IJAZAH
# =========================================================

with tab2:

    st.subheader("Verifikasi Keaslian Ijazah")

    nomor_cek = st.text_input(
        "Masukkan Nomor Ijazah",
        key="nomor_verifikasi"
    )

    if st.button("Verifikasi Ijazah"):

        if not nomor_cek.strip():

            st.warning("Nomor ijazah wajib diisi.")

        else:

            try:

                nomor_diperiksa = nomor_cek.strip()

                valid = contract.functions.cekKeaslianData(
                    nomor_diperiksa
                ).call()

                terdaftar, dicabut, status_valid = (
                    contract.functions.statusIjazah(
                        nomor_diperiksa
                    ).call()
                )

                if not terdaftar:
                    hasil_verifikasi = "Tidak ditemukan"
                    st.error("Ijazah tidak ditemukan.")
                elif dicabut:
                    hasil_verifikasi = "Sudah dicabut"
                    st.error("Ijazah sudah dicabut.")
                elif valid and status_valid:
                    hasil_verifikasi = "Valid"
                    st.success(
                        "Ijazah TERDAFTAR dan MASIH VALID."
                    )
                else:
                    hasil_verifikasi = "Tidak valid"
                    st.warning("Ijazah tidak valid.")

                # Riwayat disimpan selama sesi Streamlit ini berlangsung.
                if "riwayat_verifikasi" not in st.session_state:
                    st.session_state["riwayat_verifikasi"] = []

                st.session_state["riwayat_verifikasi"].insert(0, {
                    "Waktu": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                    "Nomor Ijazah": nomor_diperiksa,
                    "Hasil": hasil_verifikasi,
                    "Block": w3.eth.block_number
                })

            except Exception as error:

                st.error("Verifikasi gagal.")

                st.caption(str(error))


# =========================================================
# TAB 3: LIHAT DATA IJAZAH
# =========================================================

with tab3:

    st.subheader("Lihat Data Ijazah")

    nomor_data = st.text_input(
        "Masukkan Nomor Ijazah",
        key="nomor_data"
    )

    if st.button("Tampilkan Data Ijazah"):

        if not nomor_data.strip():

            st.warning("Nomor ijazah wajib diisi.")

        else:

            try:

                data = contract.functions.lihatDataIjazah(
                    nomor_data.strip()
                ).call()

                terdaftar, dicabut, valid = (
                    contract.functions.statusIjazah(
                        nomor_data.strip()
                    ).call()
                )

                if not terdaftar:

                    st.error("Ijazah tidak ditemukan.")

                else:

                    st.write("**Nama:**", data[0])

                    st.write("**NIM:**", data[1])

                    st.write("**Program Studi:**", data[2])

                    st.write("**Nomor Ijazah:**", data[3])

                    st.write("**Tahun Lulus:**", data[4])

                    if dicabut:

                        st.error("Status: SUDAH DICABUT")

                    elif valid:

                        st.success("Status: AKTIF / VALID")

                    else:

                        st.warning("Status: TIDAK VALID")

            except Exception as error:

                st.error("Data ijazah tidak ditemukan.")

                st.caption(str(error))


# =========================================================
# TAB 4: CABUT IJAZAH
# =========================================================

with tab4:

    st.subheader("Pencabutan Ijazah")

    st.caption(
        "Fitur ini hanya dapat digunakan oleh admin."
    )

    with st.form("form_cabut_ijazah"):

        nomor_cabut = st.text_input(
            "Nomor Ijazah"
        )

        alasan = st.text_area(
            "Alasan Pencabutan"
        )

        submit_cabut = st.form_submit_button(
            "Cabut Ijazah",
            type="primary"
        )

    if submit_cabut:

        if not is_admin:

            st.error(
                "Hanya admin yang dapat mencabut ijazah."
            )

        elif not nomor_cabut.strip() or not alasan.strip():

            st.warning(
                "Nomor ijazah dan alasan wajib diisi."
            )

        else:

            try:

                tx_hash = contract.functions.cabutIjazah(
                    nomor_cabut.strip(),
                    alasan.strip()
                ).transact({
                    "from": admin_address
                })

                receipt = w3.eth.wait_for_transaction_receipt(
                    tx_hash
                )

                if receipt.status == 1:

                    st.success(
                        "Ijazah berhasil dicabut."
                    )

                    st.code(tx_hash.hex())

                else:

                    st.error(
                        "Transaksi pencabutan gagal."
                    )

            except Exception as error:

                st.error("Gagal mencabut ijazah.")

                st.caption(str(error))


# =========================================================
# TAB 5: INFORMASI NFT
# =========================================================

with tab5:

    st.subheader("Informasi NFT Ijazah")

    nomor_nft = st.text_input(
        "Masukkan Nomor Ijazah",
        key="nomor_nft"
    )

    if st.button("Cek Informasi NFT"):

        if not nomor_nft.strip():

            st.warning("Nomor ijazah wajib diisi.")

        else:

            try:

                token_id = contract.functions.getTokenId(
                    nomor_nft.strip()
                ).call()

                owner = contract.functions.getOwner(
                    token_id
                ).call()

                st.write("**Token ID:**", token_id)

                st.write("**Pemilik NFT:**")

                st.code(owner)

            except Exception as error:

                st.error("NFT tidak ditemukan.")

                st.caption(str(error))

# =========================================================
# TAB 6: CETAK IJAZAH
# =========================================================

with tab6:

    st.subheader("Cetak / Unduh Ijazah")
    st.caption(
        "Ambil data ijazah dari smart contract, lalu unduh sebagai PDF."
    )

    nomor_cetak = st.text_input(
        "Masukkan Nomor Ijazah",
        key="nomor_cetak"
    )

    if st.button("Buat Dokumen Ijazah", key="buat_pdf_ijazah"):

        if not nomor_cetak.strip():
            st.warning("Nomor ijazah wajib diisi.")

        else:
            try:
                nomor_cetak_bersih = nomor_cetak.strip()

                terdaftar, dicabut, valid = (
                    contract.functions.statusIjazah(
                        nomor_cetak_bersih
                    ).call()
                )

                if not terdaftar:
                    st.error("Ijazah tidak ditemukan di blockchain.")

                else:
                    data = contract.functions.lihatDataIjazah(
                        nomor_cetak_bersih
                    ).call()

                    token_id = contract.functions.getTokenId(
                        nomor_cetak_bersih
                    ).call()

                    pemilik_nft = contract.functions.getOwner(
                        token_id
                    ).call()

                    if dicabut:
                        status_cetak = "SUDAH DICABUT"
                    elif valid:
                        status_cetak = "AKTIF / VALID"
                    else:
                        status_cetak = "TIDAK VALID"

                    buffer_pdf = BytesIO()
                    dokumen = SimpleDocTemplate(
                        buffer_pdf,
                        pagesize=A4,
                        rightMargin=2 * cm,
                        leftMargin=2 * cm,
                        topMargin=2 * cm,
                        bottomMargin=2 * cm
                    )

                    styles = getSampleStyleSheet()
                    judul_style = ParagraphStyle(
                        "JudulIjazah",
                        parent=styles["Title"],
                        alignment=TA_CENTER,
                        fontSize=18,
                        leading=23,
                        spaceAfter=12
                    )
                    subjudul_style = ParagraphStyle(
                        "SubjudulIjazah",
                        parent=styles["Normal"],
                        alignment=TA_CENTER,
                        fontSize=10,
                        leading=15
                    )

                    elemen = [
                        Paragraph("DOKUMEN DATA IJAZAH AKADEMIK", judul_style),
                        Paragraph(
                            "Dokumen informasi yang diambil dari Sistem Verifikasi "
                            "Ijazah berbasis blockchain",
                            subjudul_style
                        ),
                        Spacer(1, 1 * cm)
                    ]

                    baris_data = [
                        ["Keterangan", "Data"],
                        ["Nama Lengkap", str(data[0])],
                        ["NIM", str(data[1])],
                        ["Program Studi", str(data[2])],
                        ["Nomor Ijazah", str(data[3])],
                        ["Tahun Lulus", str(data[4])],
                        ["Token ID NFT", str(token_id)],
                        ["Pemilik NFT", str(pemilik_nft)],
                        ["Status Ijazah", status_cetak],
                        ["Alamat Smart Contract", str(CONTRACT_ADDRESS)],
                        ["Waktu Dokumen Dibuat", datetime.now().strftime("%d-%m-%Y %H:%M:%S")]
                    ]

                    # Escape data agar karakter khusus tidak merusak format PDF.
                    tabel_data = [
                        [Paragraph(escape(str(cell)), styles["BodyText"]) for cell in row]
                        for row in baris_data
                    ]

                    tabel = Table(tabel_data, colWidths=[5 * cm, 11 * cm])
                    tabel.setStyle(TableStyle([
                        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#24476B")),
                        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                        ("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("BACKGROUND", (0, 1), (0, -1), colors.HexColor("#EAF0F6")),
                        ("LEFTPADDING", (0, 0), (-1, -1), 8),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                        ("TOPPADDING", (0, 0), (-1, -1), 7),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                    ]))

                    elemen.append(tabel)
                    elemen.append(Spacer(1, 0.7 * cm))
                    elemen.append(Paragraph(
                        "Catatan: Dokumen ini merupakan keluaran aplikasi untuk "
                        "menampilkan data ijazah yang tercatat pada smart contract. "
                        "Dokumen ini bukan pengganti ijazah resmi yang diterbitkan "
                        "oleh perguruan tinggi.",
                        styles["Italic"]
                    ))

                    dokumen.build(elemen)
                    buffer_pdf.seek(0)

                    st.success("Dokumen ijazah berhasil dibuat.")
                    st.download_button(
                        label="Unduh Ijazah (PDF)",
                        data=buffer_pdf.getvalue(),
                        file_name=f"Ijazah_{nomor_cetak_bersih}.pdf",
                        mime="application/pdf"
                    )

            except Exception as error:
                st.error("Gagal membuat dokumen ijazah.")
                st.caption(str(error))


# =========================================================
# TAB 7: RIWAYAT VERIFIKASI
# =========================================================

with tab7:

    st.subheader("Riwayat Verifikasi Ijazah")
    st.caption(
        "Menampilkan pemeriksaan ijazah yang dilakukan selama sesi aplikasi Streamlit ini."
    )

    riwayat = st.session_state.get("riwayat_verifikasi", [])

    if riwayat:
        st.dataframe(
            riwayat,
            use_container_width=True,
            hide_index=True
        )

        st.info(
            "Catatan: Riwayat pada versi ini disimpan di session_state Streamlit, "
            "bukan sebagai event permanen di blockchain. Riwayat dapat hilang "
            "ketika sesi aplikxasi berakhir atau aplikasi dimulai ulang."
        )

        if st.button("Hapus Riwayat Sesi", key="hapus_riwayat"):
            st.session_state["riwayat_verifikasi"] = []
            st.rerun()

    else:
        st.info(
            "Belum ada riwayat. Lakukan pemeriksaan melalui menu Verifikasi "
            "untuk menambahkan catatan."
        )

